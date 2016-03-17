import sys

class ArabicToRoman(object):
    def __init__(self):
        self.arabic_roman_list= [("X",10), ("IX",9),("V", 5), ("IV",4)]

    def return_value(self, input_int):
        return_val = ""
        self.input_int = input_int
        for i in self.arabic_roman_list:
            if self.input_int >= i[1]:
                return_val += i[0]
                self.input_int -= i[1]

        return_val += self.handle_ones(self.input_int)
        return return_val

    def handle_ones(self, input_int):
        return_val = ""
        for i in range(input_int):
            return_val += "I"
        return return_val
