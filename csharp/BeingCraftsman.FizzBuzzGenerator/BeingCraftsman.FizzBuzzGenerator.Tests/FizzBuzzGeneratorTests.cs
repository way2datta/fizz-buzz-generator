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
    }
}
