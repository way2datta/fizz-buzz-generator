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

func PrintNumber(number int)  string {
  isDivisibleByThree := bool(number%3 == 0)

  isDivisibleByFive := bool (number%5 == 0)

  isDivisibleByBothFiveAndThree := isDivisibleByThree && isDivisibleByFive

  if isDivisibleByBothFiveAndThree {
    return ("FizzBuzz")
    } else if isDivisibleByFive {
      return ("Buzz")
    } else if isDivisibleByThree {
      return ("Fizz")
    }

    return (strconv.Itoa(number))

}

func print(number int)  {
    fmt.Println(PrintNumber(number))
}
