package main

import "math/rand"

type TestData struct{
  multipleOfThree int
  multipleOfFive int
  multipleOfThreeAndFive int
  numberNotDivisibleByFiveAndThree int
}

func randomNumberInRange(minNumber, maxNumber int) int{
  return rand.Intn(maxNumber - minNumber)+minNumber
}

func (data *TestData) assignMultipleOfThree(){
  data.multipleOfThree = randomNumberInRange(1,3)*3
}

func (data *TestData) assignMultipleOfFive(){
  data.multipleOfFive = randomNumberInRange(1,2)*5
}

func (data *TestData) assignMultipleOfThreeAndFive(){
  data.multipleOfThreeAndFive = randomNumberInRange(1,5)*3*5
}

func (data *TestData) assignNumberNotDivisibleByFiveAndThree(){
  data.numberNotDivisibleByFiveAndThree = func () int {
    for number := 0; ; number = randomNumberInRange(1,10){
      numberIsDivisibleByThree := bool (number%3 == 0)
      numberIsDivisibleByFive :=  bool (number%5 == 0)
      if !numberIsDivisibleByThree && !numberIsDivisibleByFive {
        return number
        }
    }
  }()
}
