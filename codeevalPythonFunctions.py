class Facebook_User:
    def __init__(self, user_email:str):
        self.user_email = user_email        # string given in input
        self.friends = set()                # empty set for tracking friend interactions

    def friend_action(self, friend: object):
        """
        Adds friend to set of friends, and adds self to friend's set of friends
        """
        # add friend to objects friend set, if not already in set
        self.friends.add(friend)

        # add self to friend's friend set, if not already in set
        friend.friends.add(self)


def friend_interaction(friend1:str, friend2:str, friend_dict:dict):
    """
    Creates and adds to the friend_dic a new object for each friend if one doesn't exist.
    Executes Facebook_User.friend_action for friend1
    """
    # iterate over friends
    for friend in [friend1, friend2]:

        # if string key for either friend doesn't exist, a new key and object are created and added to friend_dict
        if friend not in friend_dict:
            # Adds string version of friend to friend_dict
            friend_dict[friend] = Facebook_User(friend)

    # calls friend_action method to add each friend to the others set of friends
    friend_dict[friend1].friend_action(friend_dict[friend2])


def find_email_indexes(string:str):
    """
    Finds and returns indexes for the start of each email address
    """

    return_substrings = []  # initialize empty array to return


    # search string for '\t' char starting at the current index value
    local = string.index("@")

    # if no '\t' found, tell user and return current return_array
    if local == -1:
        print("No @ found")
        return 0,0

    # add current start of email index to return_subs-trings array
    return_substrings.append(local - 1)

    # search string for '\t' char starting at the current index value
    local = string.rindex("@")

    # if no '\t' found, tell user and return current return_array
    if local == -1:
        print("No @ found")
        return 0,0

    # add current start of email index to return_subs-trings array
    return_substrings.append(local - 1)


    # return array of found '\t' chars
    return return_substrings


def convert_indexes_to_substrings(email_indexes:list, string:str):
    """
    Converts the email start indexes pulled from find_tab_indexes to sub-strings for each facebook user
    """
    return_array = []  # initialize empty return array

    # iterate over all elements in tab array
    for i in range(len(email_indexes)):

        # check for last entry
        if i + 1 == len(email_indexes):

            # add substring of last tab char + 1 through end of string
            return_array.append(string[email_indexes[i]:])

        else:
            # add substring of tab character + 1 through next tab char in array
            return_array.append(string[email_indexes[i]: email_indexes[i + 1]])

    # iterate and strip all white space
    return_array = [r.strip() for r in return_array]

    # return array of sub-strings
    return return_array


def try_adding_friend(friend_dict: dict, friend: Facebook_User, friend_group: set):
    """
    :param friend: Facebook_User attempting add to friend_group
    :param friend_group: Group of keys to Facebook_User objects already confirmed
    :return: True if friend is able to be added, false if friend can't be added
    """

    # iterate over active friends
    for f_g in friend_group:
        #print(friend.user_email,f_g)

        # if friend isn't friends with any of the current group, return False
        if friend == friend_dict[f_g]:
            pass
        elif friend not in friend_dict[f_g].friends:
            #print("returned")
            return False

    # print(friend.user_email)
    # print("Adding to group")
    # print(friend_group)
    # if friend is friends with all other group members, return True
    return True


def recursively_add_friends(friend_dict: dict, friend_group: set, friends_available: set):
    """

    :rtype : set
    :param friend_dict: dictionary of Facebook_User objects
    :param friend_group: string keys for current friends in group
    :param friends_available: string keys for friends to try an add
    :return: largest group of friends that are all friends
    """

    if len(friends_available) == 0:
        return friend_group

    local_friends_available = friends_available.copy()


    for f_a in friends_available:

        # remove friend from local_available so it isn't recursively tried again
        local_friends_available.remove(f_a)

        # check if friend can be added to current friend_group
        if try_adding_friend(friend_dict, friend_dict[f_a], friend_group):
            # if friend is available: create a copy of local group to send recursively
            local_group = friend_group.copy()

            # add current friend to local group
            local_group.add(f_a)

            # recursively try adding more friends
            friend_group = recursively_add_friends(friend_dict, local_group, local_friends_available)

    # return largest acceptable friend_group
    return friend_group


friends = ["Thu Dec 11 17:53:01 PST 2008    a@facebook.com    b@facebook.com",
           "Thu Dec 11 17:53:02 PST 2008    b@facebook.com    a@facebook.com",
           "Thu Dec 11 17:53:03 PST 2008    a@facebook.com    c@facebook.com",
           "Thu Dec 11 17:53:04 PST 2008    c@facebook.com    a@facebook.com",
           "Thu Dec 11 17:53:05 PST 2008    b@facebook.com    c@facebook.com",
           "Thu Dec 11 17:53:06 PST 2008    c@facebook.com    b@facebook.com",
           "Thu Dec 11 17:53:07 PST 2008    d@facebook.com    e@facebook.com",
           "Thu Dec 11 17:53:08 PST 2008    e@facebook.com    d@facebook.com",
           "Thu Dec 11 17:53:09 PST 2008    d@facebook.com    f@facebook.com",
           "Thu Dec 11 17:53:10 PST 2008    f@facebook.com    d@facebook.com",
           "Thu Dec 11 17:53:11 PST 2008    e@facebook.com    f@facebook.com",
           "Thu Dec 11 17:53:12 PST 2008    f@facebook.com    e@facebook.com"]

# initialize empty dictionary of friends
friend_dict = {}

# iterate over inputs
for f in friends:
    # find the index of each '\t' in input
    tabs = find_email_indexes(f)

    # convert the tab indexes to email sub-strings
    friend1, friend2 = convert_indexes_to_substrings(tabs, f)

    # create friend objects if not already in friend_dict, and execute friend_action for friend1 and connects the two
    friend_interaction(friend1, friend2, friend_dict)
friend_groups = []

for f, k in friend_dict.items():

    # creates an empty group set starting for starting friend
    local_group = set()

    # adds current friend to that group
    local_group.add(f)

    # creates a set of all the friend string keys so each friend won't be tried after the first time
    local_available = set(friend_dict.keys())

    # removes current friend string
    local_available.remove(f)

    # attempt to add friends to group recursively
    local_group = recursively_add_friends(friend_dict, local_group, local_available)

    # if local_group has more than 3 Facebook_Users, add to friend_groups
    if len(local_group) > 2:

        # check if local_group is already in friend_groups
        if local_group not in friend_groups:

            # append
            friend_groups.append(local_group)

# empty list for adding final friend groups
final_groups = []

# iterate over valid groups
for f_g in friend_groups:

    # iterate over already final groups, to check for subset instances
    for fi_g in final_groups:

        # check if current set is subset of already added set
        if f_g.issubset(fi_g):

            # break from final group iteration and skip adding to final_group if f_g is a subset of a final group set
            break

    # convert friend group to list for sorting
    f_list = list(f_g)

    # sort friend list
    f_list.sort()

    # add sorted friend group email names as strings to final group list
    final_groups.append(", ".join(f for f in f_list))

# sort final group
final_groups.sort()

# iterate over final groups and print
for f in final_groups:
    print(f)


