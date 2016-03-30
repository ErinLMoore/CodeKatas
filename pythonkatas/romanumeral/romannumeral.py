from __future__ import division

import math
import sys

class ArabicToRoman(object):
    def __init__(self):
        self.roman_list = ['M','D','C', 'L', 'X', 'V', 'I']
        self.max_repeats_of_value = (len(self.roman_list)-1)/2
        self.value_of_highest_numeral = int(10 ** self.max_repeats_of_value)
        self.values_list = [self.value_of_highest_numeral]
        
    def return_value(self, input_int):
        self.return_val = ""
        self.input_int = input_int
        self.calculate_returns()
        return self.return_val

    def calculate_returns(self):
        for index,numeral in enumerate(self.roman_list):
            current_working_value = self.current_working_value(index)
            if self.input_int >= current_working_value:
                self.return_val += numeral * self.number_of_numerals_appended(index,current_working_value)
                self.input_int -= (current_working_value) * self.input_reducing_multiplier(index, current_working_value)
            index_offset = 2 -(index%2)
            self.handle_paired_numerals(index, numeral, current_working_value, index_offset)

    def input_reducing_multiplier(self, index, current_working_value):
        if index %2 == 1:
            return 1
        else:
            return  math.floor(self.input_int/(current_working_value))

    def handle_paired_numerals(self, index, numeral, current_working_value, index_offset):
        divisor2 =  int(math.ceil(10 ** math.ceil((index+index_offset)/2)))
        if self.input_int >= current_working_value - self.value_of_highest_numeral/divisor2:
            self.return_val  += self.roman_list[index + index_offset]+numeral
            self.input_int -= current_working_value - self.value_of_highest_numeral/divisor2

    def number_of_numerals_appended(self, index, current_working_value):
        if index %2 == 1:
            return 1
        else:
            return int(self.input_int/math.floor(current_working_value))

    def current_working_value(self, index):
        divisor =  int(math.ceil(10 ** math.ceil(index/2)))
        if index%2 == 1:
            divisor =  divisor*(.2)
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
