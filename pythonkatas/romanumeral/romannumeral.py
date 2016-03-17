import sys

class ArabicToRoman(object):
    def __init__(self):
        self.arabic_roman_multiples_list=[("C", 100), ("X",10)]
        self.arabic_roman_list= [("XL",40),("X",10), ("IX",9),("V", 5), ("IV",4)]

    def return_value(self, input_int):
        self.return_val = ""
        self.input_int = input_int

        self.handle_repeatables()
        self.handle_single_letters()
        self.handle_ones()
        return self.return_val

    def handle_repeatables(self):
        for i in self.arabic_roman_multiples_list:
            number_of_letters_to_add = self.input_int/i[1]
            if number_of_letters_to_add >=1:
                self.return_val += i[0]*number_of_letters_to_add
                self.input_int -= i[1]*number_of_letters_to_add

    def handle_single_letters(self):
        for i in self.arabic_roman_list:
            if self.input_int >= i[1]:
                self.return_val += i[0]
                self.input_int -= i[1]

    def handle_ones(self):
        for i in range(self.input_int):
            self.return_val += "I"
