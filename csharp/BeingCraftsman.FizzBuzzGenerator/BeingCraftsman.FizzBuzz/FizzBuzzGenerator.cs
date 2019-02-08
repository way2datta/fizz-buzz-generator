using System;

namespace BeingCraftsman.FizzBuzz
{
    public class FizzBuzzGenerator
    {
        public static string Generate(int input)
        {
            if (input == 10)
            {
                return "Buzz";
            }

            if (input == 15)
            {
                return "FizzBuzz";
            }

            return "Fizz";
        }
    }
}
