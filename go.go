package main

import (
	"fmt"
)

func welcome(x int) {
	fmt.Println(x)
}

// gobal level variable
var num17 int = 600

// package level variable (camel case )
var Mynum int = 800

func main() {
	// local variable

	// variable declaring way
	// var num1 int = 600
	// var num2 = 600
	// //  easy way  (only we can use it as local variable)
	// num := 700

	// var x int = 30
	// // declare and assign multiple value
	// // a,b,c := 2,3,4
	// var a,b,c int= 2,3,4
	// const z = 30
	// k := true
	// var str string = " hello world"

	// array
	// var arr = [4] int {1,2,3,4}
	// arr[2] = 49
	// arr2 := [...]int {1,2,4}  // ... daoya je jinish na dile o same kaj kore
	// nestedArray := [][]int {{1,2,3},{1,23,4,88,8}}
	// println(num)
	// println(num1)
	// println(num2,x)
	// println(a,b,c)
	// fmt.Printf("%v , %T \n",z,z)
	// println(k)
	// println(str)
	// fmt.Println(arr)  // array print korte hole fmt use korte hobe
	// fmt.Println(arr2)
	// fmt.Println(arr2[1:3])
	// fmt.Println(nestedArray)
	// fmt.Println(nestedArray[1][2])

	// loop , condition

	if 3 > 4 {
		fmt.Println("true")
	} else if 4 > 3 {
		fmt.Println("true")
	} else {

	}

	x := 2
	switch x {
	case 1:
		fmt.Println("true")

	case 2, 7:
		fmt.Println("true")
	case 3, 9:
		fmt.Println("true")
	case 4:
		fmt.Println("true")

	case 5:
		fmt.Println("true")
	}

	welcome(7)

	// struct

}
