class Fizzbuzz
  def fizzbuzzer(input_int)
    if input_int % 3 == 0
      return "fizz"
    elsif input_int % 5 == 0
      return "buzz"
    else
      return input_int
    end
  end
end
