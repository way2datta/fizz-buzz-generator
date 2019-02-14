/**
 * Fizz Buzz generator taking [input] as value
 */
fun generate(input: Int) = when {

    input.isDivisibleBy3() && input.isDivisibleBy5() -> "Fizz Buzz"

    input.isDivisibleBy3() -> "Fizz"

    input.isDivisibleBy5() -> "Buzz"

    else -> input.toString()
}

fun Int.isDivisibleBy3() = this % 3 == 0

fun Int.isDivisibleBy5() = this % 5 == 0

