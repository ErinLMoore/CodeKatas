class Fizzbuzz(object):

    def fizzbuzzer(self, input_int):
        input = input_int
        if input % 3 == 0:
            return "Buzz"
        else:
            return input
