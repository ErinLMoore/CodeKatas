import sys

class ArabicToRoman(object):

    def return_value(self, input_int):
        return_val = ""
        if input_int == 4:
            return_val = "IV"
        else:
            return_val = self.handle_ones(input_int)
        return return_val

    def handle_ones(self, input_int):
        return_val = ""
        for i in range(input_int):
            return_val += "I"
        return return_val
