# Fizz-buzz-generator
This is a fizz buzz generator using test driven development.

## Problem statement:
The Fizz buzz generator is a simple program, it's method say `generate` accepts the numeric input 
and produces the output string based on the rules and input number.

### Rules
The generate method returns the string 
- `FizzBuzz` when input parameter is divisible by 3 and 5.
- `Fizz` when input parameter is divisible by 3.
- `Buzz` when input parameter is divisible by 5.
- `String representation of given number` when input parameter neither divisible by 3 or 5.

It is clear that there are four use cases  
- **FizzBuzz**

  As a fizz buzz generator, I should be able generate a string `FizzBuzz` for given input number 
  when number is divisible by 3 and 5.

- **Fizz**

  As a fizz buzz generator, I should be able generate a string `Fizz` for given input number 
  when number is divisible by 3.
  
- **Buzz**

  As a fizz buzz generator, I should be able generate a string `Buzz` for given input number 
  when number is divisible by 5.
  
- **Number (converted to string)**

  As a fizz buzz generator, I should be able generate a string format of input number for given input number 
  when number is neither divisible by 3 or 5.
