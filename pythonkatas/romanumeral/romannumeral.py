import sys
import math

class ArabicToRoman(object):
    def __init__(self):
        self.roman_list = ['M','D','C', 'L', 'X', 'V', 'I']
        self.max_repeats_of_value = (len(self.roman_list)-1)/2
        self.value_of_highest_numeral = int(10 ** self.max_repeats_of_value)

    def return_value(self, input_int):
        self.return_val = ""
        self.input_int = input_int
        self.calculate_returns()
        return self.return_val

    def calculate_returns(self):
        for index,value in enumerate(self.roman_list):
            if self.input_int >= self.value_of_highest_numeral:
                if  int(self.input_int/self.value_of_highest_numeral)<=self.max_repeats_of_value:
                    self.return_val += value * int(self.input_int/self.value_of_highest_numeral)
                    self.input_int -= self.input_int * (self.input_int/self.value_of_highest_numeral)
                else:
                    self.return_val += value * self.value_of_highest_numeral
                    self.input_int -= self.value_of_highest_numeral * self.max_repeats_of_value

class RomantoArabic(object):
    def __init__(self):
        pass
    def return_value(self, input_string):
        return_val = input_string

        return return_val


if __name__ == '__main__':
    main = ArabicToRoman
    atr = ArabicToRoman()
    print (atr.return_value(int(sys.argv[1])))
    sys.exit(0)
