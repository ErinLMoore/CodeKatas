function fizzbuzzer(input_int) {
  var returnvar = "";
  if (input_int %3 == 0)
    {returnvar +='Fizz';}
  if (input_int %5 == 0)
      {returnvar +='Buzz';}
  if (returnvar == "")
    {returnvar = input_int;}
  return returnvar;
}
