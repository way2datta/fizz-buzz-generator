var expect = require('chai').expect;
var FizzBuzzGenerator = require('./../fizzBuzzGenerator');

describe('FizzBuzzGenerator', function () {
    it('Should return Fizz when input number is divisible by 3', () => {
        const inputArguments = [3, 6, 33];
        inputArguments.forEach(function (input) {
            const output = FizzBuzzGenerator.generate(input);
            const expectedValue = 'Fizz';
            expect(expectedValue).to.equal(output,
                `Expected '${expectedValue}' to equal '${output}' for input '${input}'`);
        });
    });

    it('Should return Buzz when input number is divisible by 5', () => {
        const inputArguments = [5, 20, 40];
        inputArguments.forEach(function (input) {
            const output = FizzBuzzGenerator.generate(input);
            const expectedValue = 'Buzz';
            expect(expectedValue).to.equal(output,
                `Expected '${expectedValue}' to equal '${output}' for input '${input}'`);
        });
    });

    it('Should return FizzBuzz when input number is divisible by 3 and 5', () => {
        const inputArguments = [15, 30, 90];
        inputArguments.forEach(function (input) {
            const output = FizzBuzzGenerator.generate(input);
            const expectedValue = 'FizzBuzz';
            expect(expectedValue).to.equal(output,
                `Expected '${expectedValue}' to equal '${output}' for input '${input}'`);
        });
    });

    it('Should return input as string when input number is neither divisible by 3 or 5', () => {
        const inputArguments = [11, 23, 26];
        inputArguments.forEach(function (input) {
            const output = FizzBuzzGenerator.generate(input);
            const expectedValue = input.toString();
            expect(expectedValue).to.equal(output,
                `Expected '${expectedValue}' to equal '${output}' for input '${input}'`);
        });
    });
});