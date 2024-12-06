package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("./t.txt")
	if err != nil {
		panic(err)
	}
	var reports [][]int

	raw := strings.Split(string(data[:len(data)-1]), "\n")

	for _, report := range raw {

		numbers := strings.Split(report, " ")
		var reportSlice []int
		for _, numstr := range numbers {
			if num, err := strconv.Atoi(numstr); err == nil {
				reportSlice = append(reportSlice, num)
			} else {
				panic(err)
			}
		}
		reports = append(reports, reportSlice)
	}

	var safe int = 0

	for i := range reports {
		if issafe(reports[i]) {
			safe++
		}
	}

	fmt.Println(safe)
}

func issafe(report []int) bool {
	var increasing bool = report[0] < report[1]
	for i := 0; i < len(report)-1; i++ {
		if increasing {
			if report[i] > report[i+1] || report[i+1]-report[i] < 1 || report[i+1]-report[i] > 3 {
				return false
			}
		} else {
			if report[i] < report[i+1] || report[i]-report[i+1] < 1 || report[i]-report[i+1] > 3 {
				return false
			}
		}
	}
	return true
}
