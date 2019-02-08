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

            return "Fizz";
        }
    }
}
