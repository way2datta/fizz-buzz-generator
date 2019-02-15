class Fizzbuzz
    def self.generate(num)
        if self.is_divisible_by_3(num) and self.is_divisible_by_5(num)
            return "fizzbuzz"
        end

        if self.is_divisible_by_3(num)
            return "fizz"
        end

        if self.is_divisible_by_5(num)
            return "buzz"
        end

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