def add(argument_string):

    if(argument_string == ""):
        return "0"
    #return str(sum([int(i) for i in argument_string.split("")]))
    new_string = argument_string.replace("\n", ",")
    string_list = new_string.split(",")
    return_string = ""
    sum = 0

    for i in string_list:
        sum += int(i)

    return str(sum)
