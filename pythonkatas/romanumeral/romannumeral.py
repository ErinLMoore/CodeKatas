import sys

class ArabicToRoman(object):
    def __init__(self):
        self.multiples_list=['C','X']
        self.arabic_roman_list= [("XC", 90),("L",50),("XL",40),("X",10),("IX",9),("V", 5), ("IV",4), ("I",1)]
        self.numerals_allowed_in_a_row= 3

    def return_value(self, input_int):
        self.return_val = ""
        self.input_int = input_int
        self.calculate_returns()
        self.handle_ones()
        return self.return_val

    def handle_repeatables(self, letter_value_pair):
        number_of_letters_to_add = self.input_int/letter_value_pair[1]
        if 1<= number_of_letters_to_add <= self.numerals_allowed_in_a_row:
            self.return_val += letter_value_pair[0]*number_of_letters_to_add
            self.input_int -= letter_value_pair[1]*number_of_letters_to_add

    def calculate_returns(self):
        for letter_value_pair in self.arabic_roman_list:
            if letter_value_pair[0] in self.multiples_list:
                self.handle_repeatables(letter_value_pair)
            else:
                if self.input_int >= letter_value_pair[1]:
                    self.return_val += letter_value_pair[0]
                    self.input_int -= letter_value_pair[1]

    def handle_ones(self):
        for i in range(self.input_int):
            self.return_val += self.arabic_roman_list[len(self.arabic_roman_list)-1][0]
