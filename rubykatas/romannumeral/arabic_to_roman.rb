

class Arabic_To_Roman
  def initialize()
    @numerals_allowed_in_a_row = 3
    @multiples_list = ["X", "I"]
    @arabic_roman_list = [["M", 1000],["CM", 900],["D",500],["CD", 400],\
          ["C", 100],["XC", 90],["L",50],["XL",40],["X",10],["IX",9],["V", 5],\
          ["IV",4], ["I",1]]
  end

  def return_value(input_int)
    @input_int = input_int
    return_value = ""
      for letter_value_pair in @arabic_roman_list
        if @multiples_list.include?(letter_value_pair[0])
          number_of_letters_to_add = @input_int/letter_value_pair[1]
          if 1<= number_of_letters_to_add and number_of_letters_to_add <= @numerals_allowed_in_a_row
            return_value += letter_value_pair[0]*number_of_letters_to_add
            @input_int -= letter_value_pair[1]*number_of_letters_to_add
          end
        end
        if @input_int - letter_value_pair[1] >= 0
          @input_int -= letter_value_pair[1]
          return_value += letter_value_pair[0]
        end
      end
    return return_value
  end

end
