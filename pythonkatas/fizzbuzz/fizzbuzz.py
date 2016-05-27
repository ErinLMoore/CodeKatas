import sys

class Fizzbuzz():

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


if __name__ == '__main__':
    main = Fizzbuzz
    fizzbuzz = Fizzbuzz()
    print (fizzbuzz.fizzbuzzer(int(sys.argv[1])))
    sys.exit(0)
