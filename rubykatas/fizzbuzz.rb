class Fizzbuzz
  def fizzbuzzer(input_int)
  case
  when input_int % 3 == 0 && input_int % 5 == 0
        return "fizzbuzz"
  when input_int % 3 == 0
    return "fizz"
  when input_int % 5 == 0
      return "buzz"
  else return input_int
  end
end
end

#add .self to fuzzbuzzer def to make runnable from command line
#puts Fizzbuzz.fizzbuzzer(ARGV[0])
