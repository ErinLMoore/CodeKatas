require 'test/unit'
require 'arabic_to_roman'

class ArabicToRomanTest < Test::Unit::TestCase
    def test_return_I_through_III
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 1
    	assert_equal expected, 'I'
      expected = atr.return_value 3
    	assert_equal expected, 'III'
    end
    def test_return_IV_for_4
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 4
    	assert_equal expected, 'IV'
    end
    def test_return_V_for_5
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 5
    	assert_equal expected, 'V'
    end
end
