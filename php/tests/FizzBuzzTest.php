<?php

use \PHPUnit\Framework\TestCase;

/**
 * Class FizzBuzzTest
 *
 * Test class for fizzbuzz generator
 */
class FizzBuzzTest extends TestCase
{

    /**
     * Test should return fizzbuzz when number is divisible by 3 and 5
     *
     * @return void
     */
    public function testShouldReturnFizzBuzzWhenNumberIsDivisibleByThreeAndFive()
    {
        $this->assertEquals("FizzBuzz", FizzBuzz::generate(15), 'Should return FizzBuzz');
    }

    /**
     * Test should return fizzbuzz when number is divisible by 3
     *
     * @return void
     */
    public function testShouldReturnFizzWhenNumberIsDivisibleByThree()
    {
        $this->assertEquals("Fizz", FizzBuzz::generate(9), 'Should return Fizz');
    }

    /**
     * Test should return buzz when number is divisible by 5
     *
     * @return void
     */
    public function testShouldReturnBuzzWhenNumberIsDivisibleByFive()
    {
        $this->assertEquals("Buzz", FizzBuzz::generate(10), 'Should return Buzz');
    }

    /**
     * Test should return number when number is not divisible by 3 and 5
     *
     * @return void
     */
    public function testShouldReturnNumberWhenNumberIsNotDivisibleByThreeAndFive()
    {
        $this->assertEquals("11", FizzBuzz::generate(11), 'Should return 11');
    }
}
