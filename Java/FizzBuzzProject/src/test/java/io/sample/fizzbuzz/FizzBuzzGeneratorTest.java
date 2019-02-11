package io.sample.fizzbuzz;

import org.junit.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsEqual.equalTo;


public class FizzBuzzGeneratorTest {

    @Test
    public void testShouldGenerateIntToString() {
        // Arrange
        int input = 2;

        // Act
        String outcome = FizzBuzzGenerator.generate(input);

        // Assert
        String expectedOutcome = "2";

        assertThat(outcome, equalTo(expectedOutcome));
    }

    @Test
    public void testPrintFizzIfNoIsDivisibleBy3() {
        // Arrange
        int input = 3;

        // Act
        String outcome = FizzBuzzGenerator.generate(input);

        // Assert
        String expectedOutcome = "fizz";

        assertThat(outcome, equalTo(expectedOutcome));
    }

    @Test
    public void testPrintBuzzIfNoIsDivisibleBy5() {
        // Arrange
        int input = 5;

        // Act
        String outcome = FizzBuzzGenerator.generate(input);

        // Assert
        String expectedOutcome = "buzz";

        assertThat(outcome, equalTo(expectedOutcome));
    }

    @Test
    public void testPrintFizzBuzzIfNoIsDivisibleByBoth() {
        // Arrange
        int input = 15;

        // Act
        String outcome = FizzBuzzGenerator.generate(input);

        // Assert
        String expectedOutcome = "fizzbuzz";

        assertThat(outcome, equalTo(expectedOutcome));
    }
}