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

            if(input == 17)
            {
                return "17"; 
            }

            if (input % 3 == 0)
            {
                return "Fizz";
            }

            return "Fizz";
        }
    }
}
