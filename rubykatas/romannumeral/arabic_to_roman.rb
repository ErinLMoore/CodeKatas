class Arabic_To_Roman

  def return_value(input_int)
    return_value = ""
    if input_int == 4
      return_value = "IV"
    else
      for i in 1..input_int
        return_value += "I"
      end
    end
    return return_value
  end
end
