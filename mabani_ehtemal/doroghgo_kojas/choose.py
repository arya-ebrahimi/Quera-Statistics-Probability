import math

def choose(n,r):
    if (n > 0 and r >= 0):
        f = math.factorial
        return f(n) / (f(r) * f(n-r))
    return 0

