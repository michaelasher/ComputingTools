"""module to calculate binomial coefficients"""

import math
import argparse

# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="total number of items to choose from")
parser.add_argument("-k", type=int, help="number of items to choose")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
parser.add_argument("-l","--log", action="store_true", help="returns the log binomial coefficient")
args = parser.parse_args()



def logfactorial(n = args.n, k = 0):
    """
    return the log of n factorial, or the log of n!/k!
    n and k are non-negative integers

    >>> logfactorial(2)
    0.6931471805599453
    
    >>> logfactorial(5,3)
    2.995732273553991

    >>> logfactorial(5,5)
    0

    >>> logfactorial(10,12)
    0

    """

    
    assert k > -1, "Error Message: k should be zero or greater"

    output = 0
    for i in range(k+1, n+1):
        output += math.log(i)
    
    return(output)
    


def choose(n = args.n,k = args.k):
    
    """
    return the binomial coefficient for n choose k
    n and k are non-negative integers

    >>> choose(10,2)
    45
    
    >>> choose(20,20)
    1

    >>> choose(24, 7)
    346104

    """
    assert n >= k, "Error Message: n should be greater than or equal to k"



    diff = n - k
    logdiff = logfactorial(diff,0)
    logquotient = logfactorial(n,k)
    logcoeff = logquotient - logdiff

    if args.log:
        print(logcoeff)
    else:
        intcoeff = round(math.exp(logcoeff))
        print(intcoeff)

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")


if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        choose()