(ns fizzbuzz.core)

(defn divisible-by? [n & nums]
  "Returns true if n is divisible by all nums."
  (reduce (fn [acc result] (and acc (zero? (rem n result)))) true nums))

(defn generate [n]
  "Returns `Fizz` if n is divisible by 3, `Buzz`
  if n is divisible by 5, `FizzBuzz` if n is divisible
  by both 3 and 5, otherwise string representation of n"
  (cond
    (divisible-by? n 3 5) "FizzBuzz"
    (divisible-by? n 3) "Fizz"
    (divisible-by? n 5) "Buzz"
    :else (str n)))