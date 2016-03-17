import sys

class ArabicToRoman(object):
    def __init__(self):
        self.roman_map = {'X':10, 'IX':9, 'V':5, 'IV':4}

    def return_value(self, input_int):
        return_val = ""
        for key,val in self.roman_map.items():
            if input_int >= val:
                return_val += key
                input_int -= val

        return_val += self.handle_ones(input_int)
        return return_val

    def handle_ones(self, input_int):
        return_val = ""
        for i in range(input_int):
            return_val += "I"
        return return_val
