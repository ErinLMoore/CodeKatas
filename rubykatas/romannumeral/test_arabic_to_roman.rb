require 'test/unit'
require 'arabic_to_roman'

class ArabicToRomanTest < Test::Unit::TestCase
    def test_return_MM
    	atr = Arabic_To_Roman.new
    	expected = atr.return_value 2000
    	assert_equal expected, 'MM'
    end

end
