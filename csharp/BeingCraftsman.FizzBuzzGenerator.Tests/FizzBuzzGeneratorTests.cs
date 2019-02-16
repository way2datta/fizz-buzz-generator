using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BeingCraftsman.FizzBuzz.Tests
{
    [TestClass]
    public class FizzBuzzGeneratorTests
    {
        [TestMethod]
        [DataRow(3)]
        [DataRow(6)]
        [DataRow(33)]
        [DataRow(99)]
        public void ShouldReturnStringFizzWhenGivenNumberIsDivisibleBy3(int input)
        {
            // Act 
            string outcome = FizzBuzzGenerator.Generate(input);

            // Assert
            string expectedOutcome = "Fizz";
            Assert.AreEqual(expectedOutcome, outcome);
        }

        [TestMethod]
        [DataRow(10)]
        [DataRow(20)]
        [DataRow(40)]
        [DataRow(100)]
        public void ShouldReturnStringBuzzWhenGivenNumberIsDivisibleBy5(int input)
        {
            // Act
            string outcome = FizzBuzzGenerator.Generate(input);

            // Assert
            string expectedOutcome = "Buzz";
            Assert.AreEqual(expectedOutcome, outcome);
        }

        [TestMethod]
        [DataRow(15)]
        [DataRow(30)]
        [DataRow(90)]
        [DataRow(150)]
        public void ShouldReturnStringFizzBuzzWhenGivenNumberIsDivisibleBy3And5(int input)
        {
            // Act
            string outcome = FizzBuzzGenerator.Generate(input);

            // Assert
            string expectedOutcome = "FizzBuzz";
            Assert.AreEqual(expectedOutcome, outcome);
        }

        [TestMethod]
        [DataRow(7)]
        [DataRow(13)]
        [DataRow(37)]
        [DataRow(133)]
        public void ShouldReturnInputAsStringWhenGivenNumberIsNeitherDivisibleBy3or5(int input)
        {
            // Act
            string outcome = FizzBuzzGenerator.Generate(input);

            // Assert
            string expectedOutcome = input.ToString();
            Assert.AreEqual(expectedOutcome, outcome);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void ShouldRaiseErrorWhenNumberIsNegative()
        {
            // Arrange
            int input = -100;

            // Act
            string outcome = FizzBuzzGenerator.Generate(input);

            // Assert: Should throw exception 
        }
    }
}
