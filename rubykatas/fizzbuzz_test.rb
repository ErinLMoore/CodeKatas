require 'test/unit'
require 'fizzbuzz'

class FizzBuzzTest < Test::Unit::TestCase
    def test_return_one_if_given_one
    	fizzbuzz = Fizzbuzz.new
    	expected = fizzbuzz.fizzbuzzer 1
    	assert_equal expected, 1
    end

    def test_return_two_if_given_two
    	fizzbuzz = Fizzbuzz.new
    	expected = fizzbuzz.fizzbuzzer 2
    	assert_equal expected, 2
    end

    def test_return_fizz_if_given_three
    	fizzbuzz = Fizzbuzz.new
    	expected = fizzbuzz.fizzbuzzer 3
    	assert_equal expected, "fizz"
    end

    def test_return_fizz_if_given_multiple_of_three
    	fizzbuzz = Fizzbuzz.new
    	expected = fizzbuzz.fizzbuzzer 6
    	assert_equal expected, "fizz"
    end

end
