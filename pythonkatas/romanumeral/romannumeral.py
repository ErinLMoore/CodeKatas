from __future__ import division

import math
import sys

class ArabicToRoman(object):
    def __init__(self):
        self.roman_list = ['M','D','C', 'L', 'X', 'V', 'I']
        self.max_repeats_of_value = (len(self.roman_list)-1)/2
        self.value_of_highest_numeral = int(10 ** self.max_repeats_of_value)
        self.values_list = self.calculate_values_list()

    def return_value(self, input_int):
        self.return_val = ""
        self.input_int = input_int
        self.calculate_returns()
        return self.return_val

    def calculate_values_list(self):
        values_list = [self.value_of_highest_numeral]
        working_val = self.value_of_highest_numeral
        for i in range (len(self.roman_list)-1):
            if i%2 ==0:
                working_val = working_val/2
            else: working_val = working_val*.2
            values_list.append(int(working_val))
        return values_list

    def calculate_returns(self):
        for index,numeral in enumerate(self.roman_list):
            current_working_value = self.values_list[index]
            if self.input_int >= current_working_value:
                self.return_val += numeral * self.number_of_numerals_to_append(index,current_working_value)
                self.input_int -= current_working_value * self.input_reducing_multiplier(index, current_working_value)
            self.handle_paired_numerals(index, numeral, current_working_value, index_offset=(2 - (index%2)))

    def handle_paired_numerals(self, index, numeral, current_working_value, index_offset):
         divisor2 =  int(math.ceil(10 ** math.ceil((index+index_offset)/2)))
         if self.input_int >= current_working_value - self.value_of_highest_numeral/divisor2:
             self.return_val  += self.roman_list[index + index_offset]+numeral
             self.input_int -= current_working_value - self.value_of_highest_numeral/divisor2


    def input_reducing_multiplier(self, index, current_working_value):
        if index %2 == 0:
            return math.floor(self.input_int/(current_working_value))
        else:
            return  1

    def number_of_numerals_to_append(self, index, current_working_value):
        if index %2 == 0:
            return int(self.input_int/math.floor(current_working_value))
        else:
            return 1

if __name__ == '__main__':
    main = ArabicToRoman
    atr = ArabicToRoman()
    print (atr.return_value(int(sys.argv[1])))
    sys.exit(0)
