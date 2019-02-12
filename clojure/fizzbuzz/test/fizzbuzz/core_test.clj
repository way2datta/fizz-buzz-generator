(ns fizzbuzz.core-test
  (:require [clojure.test :refer :all]
            [fizzbuzz.core :refer :all]
            [clojure.test.check.generators :as gen]
            [clojure.test.check.properties :as prop]
            [clojure.test.check.clojure-test :refer [defspec]]))

(defn multiple-of-n [n]
  (fn [x] (zero? (rem x n))))

(def multiple-of-3 (multiple-of-n 3))
(def multiple-of-5 (multiple-of-n 5))
(def multiple-of-15 (multiple-of-n 15))

(def not-multiple-of-3 (complement multiple-of-3))
(def not-multiple-of-5 (complement multiple-of-5))

(def multiples-of-3
  (gen/fmap #(* % 3) (gen/such-that #(and (not-multiple-of-5 %) (not= % 0)) gen/int 100)))

(def multiples-of-5
  (gen/fmap #(* % 5) (gen/such-that #(and (not-multiple-of-3 %) (not= % 0)) gen/int 100)))

(def multiples-of-15
  (gen/such-that #(and (multiple-of-15 %) (not= % 0)) gen/int 150))

(def not-multiples-of-3-or-5
  (gen/such-that #(and (not-multiple-of-5 %) (not-multiple-of-3 %)) gen/int 100))

(defspec generate-multiples-of-3-test
  (prop/for-all [n multiples-of-3]
                (= (generate n) "Fizz")))

(defspec generate-multiples-of-5-test
  (prop/for-all [n multiples-of-5]
                (= (generate n) "Buzz")))

(defspec generate-multiples-of-3-and-5-test
  (prop/for-all [n multiples-of-15]
                (= (generate n) "FizzBuzz")))

(defspec generate-not-multiples-of-3-or-5-test
  (prop/for-all [n not-multiples-of-3-or-5]
                (= (generate n) (str n))))