class Arabic_To_Roman
  def initialize()
    @roman_list = ['M','D','C','L','X','V','I']
    @values_list = [1000,500,100,50,10,5,1]
    @base_value = 10
    max_repeats_of_value = 3#(@base_value/2)-1 #EQUALS FOUR PLEASE PANIC
    @value_of_highest_numeral = @base_value ** max_repeats_of_value
    calculate_values_list
  end

  def return_value(input_int)
    return_value = ''
    for i in 0..@roman_list.length-1
      current_working_value = @values_list[i]
      current_numeral = @roman_list[i]
      return_length = (input_int/current_working_value)
      return_value += current_numeral* return_length
      input_int -= current_working_value* return_length
      subtractive_notation_index_offset=(2 - (i%2))
      divisor =  10 ** ((i+subtractive_notation_index_offset)/2).ceil
      subtractive_notation_amount = @values_list[0]/divisor
      if input_int >= current_working_value - subtractive_notation_amount
            return_value  += @roman_list[i + subtractive_notation_index_offset]+current_numeral
            input_int -= current_working_value - subtractive_notation_amount
      end
    end
    return return_value
  end
  def calculate_values_list()
    values_list = [@value_of_highest_numeral]
      working_val = @value_of_highest_numeral
      for i in 0..@roman_list.length-1
          if i%2 ==0
            working_val = working_val/2
          else working_val = working_val*( 0.2)
          end
        values_list.push( working_val)
        end
        return values_list

  end



end
