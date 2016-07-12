from log import log
def add(argument_string):

    if(argument_string == ""):
        return "0"

    delimited_string = ""

    if(argument_string[0:1] == "\\"):
        delimited_string = argument_string.split("\n", 2)[1]
        custom_delimiter = "@"
    else:
        delimited_string = argument_string
        custom_delimiter = ","
    string_list = delimited_string.replace(custom_delimiter, ",").replace("\n", ",").split(",")

    negatives_list = [i for i in string_list if "-" in i]
    if len(negatives_list)>0:
        return "negatives not allowed: " + " ".join(negatives_list)

    string_list = [i for i in string_list if int(i) <= 1000]
    results = str(sum([int(i) for i in string_list]))
    log(results)
    return  results
