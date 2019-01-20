import math


def permsubset(o, p):
    m = math.factorial(o) / math.factorial(o - p)
    return m


print("This calculates the number of permutations for a given set 'n' and subset 'r'.\n")
n = int(input("Type in 'n': \n"))
r = int(input("Type in 'r': \n"))
result = permsubset(n, r)
print(f'Your result is {result}.')
