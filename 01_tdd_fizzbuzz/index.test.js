const fizzbuzz = require("./index.js");

describe('Fizzbuzz single number tests', () => {
  test.each([
    [1, "1"],
    [2, "2"],
    [4, "4"]
  ])('[%i] returns "%i"', (num, expected) => {
      expect(fizzbuzz(num)).toEqual(expected);
    });
  test.each([
    [3],
    [6],
    [9]
  ])('%i returns "Fizz"', (num) => {
      expect(fizzbuzz(num)).toEqual("Fizz");
    });
  test.each([
    [5],
    [10],
    [20]
  ])('%i returns "Buzz"', (num) => {
      expect(fizzbuzz(num)).toEqual("Buzz");
    });
  test.each([
    [15],
    [30],
    [45]
  ])('%i returns "FizzBuzz"', (num) => {
      expect(fizzbuzz(num)).toEqual("FizzBuzz");
    });
});
