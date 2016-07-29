import sys

sys.path.append('~/workspace/CodeKatas/pythonkatas/packagepractice')

import mymath
class main ():
    print sys.argv
    v = sys.argv[1].lower()
    valOne = int(sys.argv[2])
    valTwo = int(sys.argv[3])
    if v == "a":
        print mymath.add(valOne, valTwo)
    elif v == "d":
        print mymath.division(valOne, valTwo)
    elif v == "m":
        print mymath.multiply(valOne, valTwo)
    elif v == "s":
        print mymath.subtract(valOne, valTwo)
    else:
        pass
