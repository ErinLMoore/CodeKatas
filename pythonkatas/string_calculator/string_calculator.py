def add(argument_string):
    string_list = argument_string.split(",")
    if len(string_list)==1:
        if argument_string == "":
            return "0"
        else:
            return argument_string
    else:
        return  str(int(string_list[0]) + int(string_list[1]))
