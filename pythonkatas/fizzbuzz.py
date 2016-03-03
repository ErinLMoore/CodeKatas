class Fizzbuzz(object):

    def fizzbuzzer(self, input_int):
        input = input_int
        if input % 15 == 0:
            return "FizzBuzz"
        if input % 3 == 0:
            return "Buzz"
        if input % 5 == 0:
            return "Fizz"
        else:
            return input
