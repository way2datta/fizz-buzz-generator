require_relative "../fizzbuzz.rb"
require "test/unit"

class TestFizzBuzz < Test::Unit::TestCase

    def test_should_print_fizzbuzz_when_divisible_by_three_and_five
        assert_equal("fizzbuzz", Fizzbuzz.generate(15))
    end

    def test_should_print_fizz_when_divisible_by_only_three
        assert_equal("fizz", Fizzbuzz.generate(9))
    end

    def test_should_print_buzz_when_divisible_by_only_five
        assert_equal("buzz", Fizzbuzz.generate(10))
    end

    def test_should_print_number_as_string_when_no_divisible_by_three_or_five
        assert_equal("4", Fizzbuzz.generate(4))
    end
    
end