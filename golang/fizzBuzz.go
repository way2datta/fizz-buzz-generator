package main

import (
  "fmt"
  "strconv"
)


func main() {
  for i:=0; i<=100; i++ {
    print(i)
  }
}

func print(number int)  {
    fmt.Println(FizzBuzzGenerator(number))
}

func FizzBuzzGenerator(number int)  string {
  if numberIsDivisibleByThree(number) && numberIsDivisibleByFive(number) {
    return ("FizzBuzz")
    }
  if numberIsDivisibleByFive(number) {
    return ("Buzz")
  }
  if numberIsDivisibleByThree(number) {
    return ("Fizz")
  }

  return (strconv.Itoa(number))

}

func numberIsDivisibleByThree(number int) bool {
  return number%3 ==0
}

func numberIsDivisibleByFive(number int) bool {
  return number%5 ==0
}
