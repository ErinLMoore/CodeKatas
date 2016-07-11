def add(argument_string):

    if(argument_string == ""):
        return "0"
    return str(sum([int(i) for i in argument_string.split(",")]))
