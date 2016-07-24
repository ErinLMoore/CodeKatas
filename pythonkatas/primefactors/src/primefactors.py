def primeFactors(argint):
    returnlist = [argint]
    for i in range(1,argint):
        if argint % i == 0:
            returnlist.append(i)
    return sorted(returnlist)
