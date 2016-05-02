require 'test/unit'
require 'arabic_to_roman'

class ArabicToRomanTest < Test::Unit::TestCase
    def test_return_MM_for_2000
    	atr = Arabic_To_Roman.new
      expected = 'MM'
    	actual = atr.return_value 2000
    	assert_equal expected, actual
    end

    def test_return_CC_for_200
    	atr = Arabic_To_Roman.new
      expected = 'CC'
    	actual = atr.return_value 200
    	assert_equal expected, actual
    end

    def test_return_XX_for_20
    	atr = Arabic_To_Roman.new
      expected = 'XX'
    	actual = atr.return_value 20
    	assert_equal expected, actual
    end

    def test_return_II_for_2
    	atr = Arabic_To_Roman.new
      expected = 'II'
    	actual = atr.return_value 2
    	assert_equal expected, actual
    end

    def test_return_D_for_500
    	atr = Arabic_To_Roman.new
      expected = 'D'
    	actual = atr.return_value 500
    	assert_equal expected, actual
    end

    def test_return_L_for_50
    	atr = Arabic_To_Roman.new
      expected = 'L'
    	actual = atr.return_value 50
    	assert_equal expected, actual
    end

    def test_return_V_for_5
    	atr = Arabic_To_Roman.new
      expected = 'V'
    	actual = atr.return_value 5
    	assert_equal expected, actual
    end

    def test_return_MMDCCLXXVII_for_2777
    	atr = Arabic_To_Roman.new
      expected = 'MMDCCLXXVII'
    	actual = atr.return_value 2777
    	assert_equal expected, actual
    end

    def test_return_CM_for_900
    	atr = Arabic_To_Roman.new
      expected = 'CM'
    	actual = atr.return_value 900
    	assert_equal expected, actual
    end

    def test_return_CD_for_400
      atr = Arabic_To_Roman.new
      expected = 'CD'
      actual = atr.return_value 400
      assert_equal expected, actual
    end

    def test_return_XC_for_90
      atr = Arabic_To_Roman.new
      expected = 'XC'
      actual = atr.return_value 90
      assert_equal expected, actual
    end

    def test_return_XL_40
      atr = Arabic_To_Roman.new
      expected = 'XL'
      actual = atr.return_value 40
      assert_equal expected, actual
    end

    def test_return_IX_for_9
      atr = Arabic_To_Roman.new
      expected = 'IX'
      actual = atr.return_value 9
      assert_equal expected, actual
    end

    def test_return_IV_for_4
      atr = Arabic_To_Roman.new
      expected = 'IV'
      actual = atr.return_value 4
      assert_equal expected, actual
    end

    def test_return_MMMCMXCIX_for_3999
      atr = Arabic_To_Roman.new
      expected = 'MMMCMXCIX'
      actual = atr.return_value 3999
      assert_equal expected, actual
    end

end
