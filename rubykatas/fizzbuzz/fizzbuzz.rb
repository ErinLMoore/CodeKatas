class Fizzbuzz
  def fizzbuzzer(input_int)
  return_value = ""
  if input_int % 3 == 0
        return_value += "fizz"
  end
  if input_int % 5 == 0
      return_value += "buzz"
  end
  if return_value == ""
    return_value = input_int
  end
  return return_value
end
end

#add .self to fuzzbuzzer def to make runnable from command line
#puts Fizzbuzz.fizzbuzzer(ARGV[0])
