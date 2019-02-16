<?php

/**
 * Class FizzBuzz
 *
 * FizzBuzz generator class
 */
class FizzBuzz {

    /**
     * Generate fizzbuzz from given number
     *
     * @param int $number number to generate fizzbuzz
     *
     * @return string
     */
    public static function generate(int $number) : string
    {

        if (self::isDivisibleBy3($number) && self::isDivisibleBy5($number)) return "FizzBuzz";

        if (self::isDivisibleBy3($number)) return "Fizz";

        if (self::isDivisibleBy5($number)) return "Buzz";

        return $number;
    }

    /**
     * Check if number is divisible by 3
     *
     * @param int $number number to check
     *
     * @return bool
     */
    private static function isDivisibleBy3(int $number) : bool
    {
        return $number % 3 === 0;
    }

    /**
     * Check if number is divisible by 5
     *
     * @param int $number number to check
     *
     * @return bool
     */
    private static function isDivisibleBy5(int $number) : bool
    {
        return $number % 5 === 0;
    }
}
