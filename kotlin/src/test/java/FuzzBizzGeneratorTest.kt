package test.java

import generate
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

class FuzzBizzGeneratorTest {

    @Test
    fun `test If number is divisible by three and five and return fizz buzz`() {
        val input = 15
        val output = generate(input)
        assertEquals(output, "Fizz Buzz")
    }

    @Test
    fun `test If number is divisible by three and return fizz`() {
        val input = 9
        val output = generate(input)
        assertEquals(output, "Fizz")
    }

    @Test
    fun `test If number is divisible by three and return buzz`() {
        val input = 10
        val output = generate(input)
        assertEquals(output, "Buzz")
    }

    @Test
    fun `test If number is not divisible by three and five return the number`() {
        val input = 11
        val output = generate(input)
        assertEquals(output, input.toString())
    }

}