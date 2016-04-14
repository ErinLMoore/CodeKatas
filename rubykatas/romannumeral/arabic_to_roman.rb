class Arabic_To_Roman
  def initialize()
    @roman_list = ['M','C','X','I']
    @values_list = [1000,100,10,1]
  end

  def return_value(input_int)
    return_value = ''
    for i in 0..@roman_list.length-1
      if input_int/@values_list[i] != 0
        return_length = (input_int/@values_list[i])
        return_value = @roman_list[i]* return_length
        input_int -= @values_list[i]* return_length
      end
    end
    return return_value
  end
end
