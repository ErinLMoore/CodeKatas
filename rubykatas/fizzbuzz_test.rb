require 'test/unit'
require 'fizzbuzz'
class FizzBuzzTest < Test::Unit::TestCase
    def test_return_one_if_given_one
    	fizzbuzz = Fizzbuzz.new
    	expected = fizzbuzz.fizzbuzzer 1
    	assert_equal expected, 1
    end
end
