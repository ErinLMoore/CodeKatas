from __future__ import division

import math
import sys

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
            if index == 0 or index%2 == 0:
                divisor =  int(math.ceil(10 ** math.ceil(index/2)))
                divisor2 =  int(math.ceil(10 ** math.ceil((index+2)/2)))
                if self.input_int >= self.value_of_highest_numeral/divisor:
                    self.return_val += value * int(self.input_int/math.floor(self.value_of_highest_numeral/divisor))
                    self.input_int -= (self.value_of_highest_numeral/divisor) * math.floor(self.input_int/(self.value_of_highest_numeral/divisor))
                if self.input_int >= self.value_of_highest_numeral/divisor - self.value_of_highest_numeral/divisor2:
                    self.return_val  += self.roman_list[index + 2]+value
                    self.input_int -= self.value_of_highest_numeral/divisor - self.value_of_highest_numeral/divisor2
            else:
                divisor =  int(math.ceil(10 ** math.ceil(index/2)))*(.2)
                divisor2 =  int(math.ceil(10 ** math.ceil((index+1)/2)))
                if self.input_int >= self.value_of_highest_numeral/divisor:
                    self.return_val += value
                    self.input_int -= self.value_of_highest_numeral/divisor
                if self.input_int >= self.value_of_highest_numeral/divisor - self.value_of_highest_numeral/divisor2:
                    self.return_val  += self.roman_list[index + 1]+value
                    self.input_int -= self.value_of_highest_numeral/divisor - self.value_of_highest_numeral/divisor2



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
