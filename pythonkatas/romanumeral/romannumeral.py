import sys

class ArabicToRoman(object):

    def return_value(self, input_int):
        return_val = ""
        for i in range(input_int):
            return_val += "I"
        return return_val
