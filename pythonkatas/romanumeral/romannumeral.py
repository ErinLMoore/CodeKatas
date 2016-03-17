import sys

class ArabicToRoman(object):
    def __init__(self):
        self.arabic_roman_multiples_list=[("C", 100), ("X",10)]
        self.arabic_roman_list= [("XL",40),("X",10), ("IX",9),("V", 5), ("IV",4)]

    def return_value(self, input_int):
        return_val = ""
        self.input_int = input_int

        for i in self.arabic_roman_multiples_list:
            number_of_letters_to_add = input_int/i[1]
            if number_of_letters_to_add >=1:
                return_val += i[0]*number_of_letters_to_add
                self.input_int -= i[1]*number_of_letters_to_add

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
