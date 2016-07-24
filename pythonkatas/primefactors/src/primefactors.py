def primeFactors(argint):

    for i in xrange(2, argint):
        if argint % i == 0:
            return [i] + primeFactors(argint/i)

    return [argint]
