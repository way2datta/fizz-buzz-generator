using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BeingCraftsman.FizzBuzz.Tests
{
    [TestClass]
    public class FizzBuzzGeneratorTests
    {
        [TestMethod]
        public void ShouldReturnStringFizzWhenGivenNumberIsDivisibleBy3()
        {
            int input = 3;
            string actual = FizzBuzzGenerator.Generate(input);
            string expected = "Fizz";
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ShouldReturnStringBuzzWhenGivenNumberIsDivisibleBy5()
        {
            int input = 10;
            string actual = FizzBuzzGenerator.Generate(input);
            string expected = "Buzz";
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ShouldReturnStringFizzBuzzWhenGivenNumberIsDivisibleBy3And5()
        {
            int input = 15;
            string actual = FizzBuzzGenerator.Generate(input);
            string expected = "FizzBuzz";
            Assert.AreEqual(expected, actual);
        }
    }
}
