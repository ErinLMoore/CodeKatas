class Fizzbuzz(object):

    def fizzbuzzer(self, input_int):
        input = input_int
        returnitem = ""
        if input % 5 == 0:
            returnitem += "Fizz"
        if input % 3 == 0:
            returnitem += "Buzz"
        if returnitem == "":
            returnitem = input
        return returnitem
