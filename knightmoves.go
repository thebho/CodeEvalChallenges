package main

import (
	"fmt"
	"strconv"
)

type Position struct {
	row int
	col string
}

func (p Position) TestDirections() []string {
	answers := make([]string, 0)
	var newRow int
	var newCol int
	colInt := int(p.col[0])
	// NE
	if newRow = p.row + 2; newRow < 8 {
		if newCol = colInt + 1; newCol < 105 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	// EN
	if newRow = p.row + 1; newRow < 8 {
		if newCol = colInt + 2; newCol < 105 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)

		}
	}
	// ES
	if newRow = p.row - 1; newRow > 0 {
		if newCol = colInt + 2; newCol < 105 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	// SE
	if newRow = p.row - 2; newRow > 0 {
		if newCol = colInt + 1; newCol < 105 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	// SW
	if newRow = p.row - 2; newRow > 0 {
		if newCol = colInt - 1; newCol > 96 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	// WS
	if newRow = p.row - 1; newRow > 0 {
		if newCol = colInt - 2; newCol > 96 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	// WN
	if newRow = p.row + 1; newRow < 105 {
		if newCol = colInt - 2; newCol > 96 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	// NW
	if newRow = p.row + 2; newRow < 105 {
		if newCol = colInt - 1; newCol > 96 {
			colRune := rune(newCol)
			ans := fmt.Sprintf("%s%d", string(colRune), newRow)
			answers = append(answers, ans)
		}
	}
	return answers
}

var testCases = []string{"g2",
	"a1",
	"d6",
	"e5",
	"b1"}

// Converts "(a5,d2,c3)" to
func convertToPosition(s string) (*Position, error) {
	if len(s) != 2 {
		return nil, fmt.Errorf("Argument to converToPosition not valid position string: %s", s)
	}
	letter := string(s[0])
	number, err := strconv.Atoi(string(s[1]))
	if err != nil {
		return nil, fmt.Errorf("Second char not an int %s, %v", s, err)
	}
	return &Position{
		col: letter,
		row: number,
	}, nil
}

func printSortedArray(arr []string) {
	arrCopy := arr
	printed := false
	for {
		if len(arrCopy) == 1 {
			if printed {
				fmt.Print(" ")
			}
			fmt.Println(arrCopy[0])
			return
		}
		toPrint := 0
		for i := range arrCopy {
			if arr[i] < arr[toPrint] {
				toPrint = i
			}
		}
		if printed {
			fmt.Print(" ")
		}
		printed = true
		fmt.Print(arrCopy[toPrint])
		arrCopy = append(arrCopy[:toPrint], arrCopy[toPrint+1:]...)
	}
}

func main() {
	// file, err := os.Open(os.Args[1])
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// defer file.Close()
	// scanner := bufio.NewScanner(file)
	// for scanner.Scan() {
	for _, t := range testCases {
		position, err := convertToPosition(t)
		if err != nil {
			fmt.Println(err)
			continue
		}
		answers := position.TestDirections()
		printSortedArray(answers)
	}
}
