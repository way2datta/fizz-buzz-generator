class Fizzbuzz
    def self.generate(num)
        return "fizzbuzz" if self.is_divisible_by_3(num) and self.is_divisible_by_5(num)

        return "fizz" if self.is_divisible_by_3(num)

        return "buzz" if self.is_divisible_by_5(num)

        num.to_s
    end

    private
    def self.is_divisible_by_3(num)
        num % 3 == 0
    end

    def self.is_divisible_by_5(num)
        num % 5 == 0
    end
end