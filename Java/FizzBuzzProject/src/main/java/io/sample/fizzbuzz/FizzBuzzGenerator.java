package io.sample.fizzbuzz;

public class FizzBuzzGenerator {
    public static String generate(int value) {
        if (isDivisibleBy3(value) && isDivisibleBy5(value)) {
            return "fizzbuzz";
        } else if (isDivisibleBy3(value)) {
            return "fizz";
        } else if (isDivisibleBy5(value)) {
            return "buzz";
        }
        return String.valueOf(value);
    }

    private static boolean isDivisibleBy3(int value) {
        return value % 3 == 0;
    }

    private static boolean isDivisibleBy5(int value) {
        return value % 5 == 0;
    }
}
