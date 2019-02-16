namespace BeingCraftsman.FizzBuzz
{
    public static class FizzBuzzGenerator
    {
        public static string Generate(int input)
        {
            if (IsDivisibleBy5(input) && IsDivisibleBy3(input))
            {
                return "FizzBuzz";
            }

            if (IsDivisibleBy3(input))
            {
                return "Fizz";
            }

            if (IsDivisibleBy5(input))
            {
                return "Buzz";
            }

            return input.ToString();
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
