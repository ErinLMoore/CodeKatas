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
    def test_return_unique_singles
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 4
    	assert_equal expected, 'IV'
      expected = atr.return_value 5
    	assert_equal expected, 'V'
      expected = atr.return_value 9
      assert_equal expected, 'IX'
    end

    def test_return_VI_through_VII
      atr = Arabic_To_Roman.new
      expected = atr.return_value 6
      assert_equal expected, 'VI'
      expected = atr.return_value 8
      assert_equal expected, 'VIII'
    end
end
