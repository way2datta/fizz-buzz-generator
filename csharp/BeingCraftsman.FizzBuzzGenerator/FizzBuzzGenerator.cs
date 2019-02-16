using System;

namespace BeingCraftsman.FizzBuzz
{
    public static class FizzBuzzGenerator
    {
        public static string Generate(int value)
        {
            if (value < 0)
            {
                var errorMessage = $"{value} is not a positive number.";
                throw new ArgumentException(errorMessage);
            }

            if (IsDivisibleBy5(value) && IsDivisibleBy3(value))
            {
                return "FizzBuzz";
            }

            if (IsDivisibleBy3(value))
            {
                return "Fizz";
            }

            if (IsDivisibleBy5(value))
            {
                return "Buzz";
            }

            return value.ToString();
        }

        private static bool IsDivisibleBy3(int input)
        {
            return input % 3 == 0;
        }

        private static bool IsDivisibleBy5(int input)
        {
            return input % 5 == 0;
        }
    }
}
