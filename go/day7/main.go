package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func generateCombinations(ops []string, length int) [][]string {
	if length == 0 {
		return [][]string{{}}
	}

	smaller := generateCombinations(ops, length-1)
	var result [][]string

	for _, seq := range smaller {
		for _, op := range ops {
			newSeq := append([]string{}, seq...)
			newSeq = append(newSeq, op)
			result = append(result, newSeq)
		}
	}
	return result
}

func solve(key int, values []int) bool {
	operators := []string{"*", "+", "|"}

	combinations := generateCombinations(operators, len(values)-1)

	for _, combo := range combinations {
		ans := values[0]
		for i := 1; i < len(values); i++ {
			switch combo[i-1] {
			case "+":
				ans += values[i]
			case "|":
				ans, _ = strconv.Atoi(fmt.Sprintf("%d%d", ans, values[i]))
			case "*":
				ans *= values[i]
			}
		}
		if ans == key {
			return true
		}
	}
	return false
}

func main() {
	data, err := os.ReadFile("./t.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	finalNums := make(map[int][]int)

	for _, line := range lines {
		parts := strings.Split(line, ": ")
		key, _ := strconv.Atoi(parts[0])
		valuesStr := strings.Fields(parts[1])
		var values []int

		for _, v := range valuesStr {
			num, _ := strconv.Atoi(v)
			values = append(values, num)
		}
		finalNums[key] = values
	}

	ans2 := 0
	for key, values := range finalNums {
		if solve(key, values) {
			ans2 += key
		}
	}

	fmt.Printf("Sum of keys that satisfy the condition: %d\n", ans2)
}
