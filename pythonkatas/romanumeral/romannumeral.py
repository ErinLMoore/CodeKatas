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
                current_working_value = self.current_working_value(index)
                divisor2 =  int(math.ceil(10 ** math.ceil((index+2)/2)))
                if self.input_int >= current_working_value:
                    self.return_val += value * int(self.input_int/math.floor(current_working_value))
                    self.input_int -= (current_working_value) * math.floor(self.input_int/(current_working_value))
                self.handle_paired_numerals(index, value, current_working_value, divisor2, 2)

            else:
                current_working_value = self.current_working_value(index)
                divisor2 =  int(math.ceil(10 ** math.ceil((index+1)/2)))
                if self.input_int >= current_working_value:
                    self.return_val += value
                    self.input_int -= current_working_value
                self.handle_paired_numerals(index, value, current_working_value, divisor2, 1)


    def handle_paired_numerals(self, index, value, current_working_value, divisor2, index_offset):
        if self.input_int >= current_working_value - self.value_of_highest_numeral/divisor2:
            self.return_val  += self.roman_list[index + index_offset]+value
            self.input_int -= current_working_value - self.value_of_highest_numeral/divisor2

    def current_working_value(self, index):
        if index == 0 or index%2 == 0:
            divisor =  int(math.ceil(10 ** math.ceil(index/2)))
        else: divisor =  int(math.ceil(10 ** math.ceil(index/2)))*(.2)
        return self.value_of_highest_numeral/divisor


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
