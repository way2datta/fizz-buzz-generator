package test.java

import generate
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

class FuzzBizzGeneratorTest {

    @Test
    fun `when the number is divisible by three and five then return fizz buzz`() {

        // Arrange
        val input = 15

        // Act
        val output = generate(input)

        // Assert
        assertEquals(output, "Fizz Buzz")
    }

    @Test
    fun `when the number is divisible by three then return fizz`() {

        // Arrange
        val input = 9

        // Act
        val output = generate(input)

        // Assert
        assertEquals(output, "Fizz")
    }

    @Test
    fun `when the number is divisible by five then return buzz`() {

        // Arrange
        val input = 10

        // Act
        val output = generate(input)

        // Assert
        assertEquals(output, "Buzz")
    }

    @Test
    fun `when the number is not divisible by three and five then return the number in string`() {

        // Arrange
        val input = 11

        // Act
        val output = generate(input)

        // Assert
        assertEquals(output, input.toString())
    }

}