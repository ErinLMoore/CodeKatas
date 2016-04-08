class Arabic_To_Roman
  def initialize()
  end

  def return_value(input_int)
    @input_int = input_int
    @return_length = @input_int/1000
    @return_value = 'M'* @return_length
    return @return_value
  end
end
