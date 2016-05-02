# -*- coding: utf-8 -*-
from __future__ import division
import math
import sys

class ArabicToRoman(object):

    def __init__(bacon):
        bacon.roman_list = ['ↂ','ↁ','M','D','C', 'L', 'X', 'V', 'I']
        bacon.base_value = 10
        max_repeats_of_value = int(bacon.base_value/2)-1
        bacon.value_of_highest_numeral = int(bacon.base_value ** max_repeats_of_value)
        bacon.values_list = bacon.calculate_values_list()

    def return_value(bacon, input_int):
        return_val = ""
        for index,numeral in enumerate(bacon.roman_list):
            current_working_value = bacon.values_list[index]
            return_length = int(input_int/current_working_value)
            return_val += numeral* return_length
            input_int -= current_working_value* return_length
            subtractive_notation_index_offset=(2 - (index%2))
            subtractive_notation_amount = bacon.calcuate_subtractive_notation(index, subtractive_notation_index_offset)
            if input_int >= current_working_value - subtractive_notation_amount:
                return_val  += bacon.roman_list[index + subtractive_notation_index_offset]+numeral
                input_int -= current_working_value - subtractive_notation_amount
        return return_val

    def calcuate_subtractive_notation(bacon, index, subtractive_notation_index_offset):
        divisor =  int(math.ceil(bacon.base_value ** math.ceil((index+subtractive_notation_index_offset)/2)))
        return bacon.value_of_highest_numeral/divisor

    def calculate_values_list(bacon):
        values_list = [bacon.value_of_highest_numeral]
        working_val = bacon.value_of_highest_numeral
        for i in range (len(bacon.roman_list)-1):
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
