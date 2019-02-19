package main

import (
      "testing"
      "math/rand"
      "strconv"
      "time"
      "os"
    )


func TestMain(m *testing.M){
  rand.Seed(time.Now().UnixNano())
  os.Exit(m.Run())
}

func TestFizzWhenInputIsDivisibleByThree(t *testing.T){
  data  := TestData{0,0,0,0}
  data.assignMultipleOfThree()

  stringReturned := FizzBuzzGenerator(data.multipleOfThree)

  expectedString := "Fizz"
  if stringReturned != expectedString {
    t.Errorf("It should print Fizz for number %d since it is divisible by 3", data.multipleOfThree)
  }
}

func TestBuzzWhenInputIsDivisibleByFive(t *testing.T){
  data  := TestData{0,0,0,0}
  data.assignMultipleOfFive()

  stringReturned := FizzBuzzGenerator(data.multipleOfFive)
  expectedString := "Buzz"
  if stringReturned != expectedString {
    t.Errorf("It should print Buzz for number %d since it is divisible by 5", data.multipleOfFive)
  }
}

func TestFizzBuzzWhenInputIsDivisibleByFiveAndThree(t *testing.T){
  data  := TestData{0,0,0,0}
  data.assignMultipleOfThreeAndFive()

  stringReturned := FizzBuzzGenerator(data.multipleOfThreeAndFive)
  expectedString := "FizzBuzz"

  if stringReturned != expectedString {
    t.Errorf("It should print FizzBuzz for number %d since it is divisible by 3 and 5", data.multipleOfThreeAndFive)
  }
}

func TestShouldPrintTheNumberWhenItIsNeitherDivisibleByThreeAndFive(t *testing.T){
  data  := TestData{0,0,0,0}
  data.assignNumberNotDivisibleByFiveAndThree()

  stringReturned := FizzBuzzGenerator(data.numberNotDivisibleByFiveAndThree)
  expectedString := strconv.Itoa(data.numberNotDivisibleByFiveAndThree)

  if expectedString != stringReturned {
    t.Errorf("It should print the number since number is not divisible by 3 and 5")
  }
}

func TestShouldDivideMultipleOfThree(t *testing.T){
  data  := TestData{0,0,0,0}
  data.assignMultipleOfThree()

  if !numberIsDivisibleByThree(data.multipleOfThree) {
    t.Errorf("Multiple of three is not divided")
  }
}

func TestShouldDivideMultipleOfFive(t *testing.T){
  data  := TestData{0,0,0,0}
  data.assignMultipleOfFive()

  if !numberIsDivisibleByFive(data.multipleOfFive) {
    t.Errorf("Multiple of five is not divided")
  }
}
