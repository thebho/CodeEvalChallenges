__author__ = 'brianhoehne'

MONTH = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

test_cases = ["Feb 2004-Dec 2009; Sep 2004-Jul 2008",
              "Aug 2013-Mar 2014; Apr 2013-Aug 2013; Jun 2014-Aug 2015; Apr 2003-Nov 2004; Apr 2014-Jan 2015",
              "Mar 2003-Jul 2003; Nov 2003-Jan 2004; Apr 1999-Nov 1999",
              "Apr 1992-Dec 1993; Feb 1996-Sep 1997; Jan 2002-Jun 2002; Sep 2003-Apr 2004; Feb 2010-Nov 2011",
              "Feb 2004-May 2004; Jun 2004-Jul 2004"]

def update_job_dict(job_dict, job):
    for year in job.active_years:
        if year not in job_dict:
            job_dict[year] = set()
        if year == job.start_year:
            if year == job.end_year:
                for i in range(job.start_month, job.end_month + 1):
                    job_dict[year].add(i)
            else:
                for i in range(job.start_month, 13):
                    job_dict[year].add(i)
        elif year == job.end_year:
            for i in range(1, job.end_month + 1):
                job_dict[year].add(i)
        else:
            job_dict[year] = set(list(range(1, 13)))
    return job_dict

def calculate_work_exp(job_dict):
    ans = 0
    for k,v in job_dict.items():
        ans += len(v)
    return ans//12

def string_to_month_year(string):
    month = string[:3]
    year = int(string[4:])
    return MONTH[month],year

class Job:
    def __init__(self, dates):
        start_date = dates[:8]
        end_date = dates[9:]
        self.active_years = []

        self.start_month, self.start_year = string_to_month_year(start_date)
        self.end_month, self.end_year = string_to_month_year(end_date)
        for i in range(self.start_year, self.end_year + 1):
            self.active_years.append(i)

        #print(self.active_years)

for test in test_cases:
    #initiate empty job dict
    jobs_dict = {}
    #separate into date sequences
    index = 0
    while True:
        semi_colon = test.find(";",index)
        if semi_colon > -1:
            job = Job(test[index:semi_colon])
            jobs_dict = update_job_dict(jobs_dict, job)
            index = semi_colon + 2
        else:
            job = Job(test[index:])
            jobs_dict = update_job_dict(jobs_dict, job)
            index = semi_colon + 2
            break
    print(calculate_work_exp(jobs_dict))
