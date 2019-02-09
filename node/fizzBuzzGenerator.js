class FizzBuzzGenerator {
    static generate(input) {
        const isDivisibleBy3 = (value) => value % 3 === 0;
        const isDivisibleBy5 = (value) => value % 5 === 0;

        if(isDivisibleBy3(input) && isDivisibleBy5(input)) {
            return 'FizzBuzz';
        }
        if(isDivisibleBy3(input)) {
            return 'Fizz';
        }
        if(isDivisibleBy5(input)) {
            return 'Buzz';
        }
        return input.toString();
    } 
}

module.exports = FizzBuzzGenerator;