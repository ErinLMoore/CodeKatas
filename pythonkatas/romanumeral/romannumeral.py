# -*- coding: utf-8 -*-
from __future__ import division
import math
import sys

class ArabicToRoman(object):
    def __init__(self):
        self.roman_list = ['ↂ','ↁ','M','D','C', 'L', 'X', 'V', 'I']
        base_value = 10
        max_repeats_of_value = int(base_value/2)-1
        self.value_of_highest_numeral = int(base_value ** max_repeats_of_value)
        self.values_list = self.calculate_values_list()

    def return_value(self, input_int):
        return_val = ""
        for index,numeral in enumerate(self.roman_list):
            current_working_value = self.values_list[index]
            if input_int >= current_working_value:
                return_val += numeral * self.number_of_numerals_to_append(input_int,index)
                input_int -= current_working_value * self.input_reducing_multiplier(input_int,index)
            subtractive_notation_index_offset=(2 - (index%2))
            subtractive_notation_amount = self.calcuate_subtractive_notation(index, subtractive_notation_index_offset)
            if input_int >= current_working_value - subtractive_notation_amount:
                return_val  += self.roman_list[index + subtractive_notation_index_offset]+numeral
                input_int -= current_working_value - subtractive_notation_amount
        return return_val

    def input_reducing_multiplier(self, input_int,index):
        if index %2 == 0:
            return math.floor(input_int/( self.values_list[index]))
        else:
            return  1

    def number_of_numerals_to_append(self, input_int, index):
        if index %2 == 0:
            return int(input_int/math.floor(self.values_list[index]))
        else:
            return 1

    def calcuate_subtractive_notation(self,index, subtractive_notation_index_offset):

        divisor =  int(math.ceil(10 ** math.ceil((index+subtractive_notation_index_offset)/2)))
        return self.value_of_highest_numeral/divisor

    def calculate_values_list(self):
        values_list = [self.value_of_highest_numeral]
        working_val = self.value_of_highest_numeral
        for i in range (len(self.roman_list)-1):
            if i%2 ==0:
                working_val = working_val/2
            else: working_val = working_val*.2
            values_list.append(int(working_val))
        return values_list

if __name__ == '__main__':
    main = ArabicToRoman
    atr = ArabicToRoman()
    print (atr.return_value(int(sys.argv[1])))
    sys.exit(0)
