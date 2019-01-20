import math


def denominator_calc(o, p):
    return math.factorial(p) * math.factorial(o - p)


print("This calculates the number of permutations for a given set 'n' and subset 'r'.\n")


n = int(input("Type in n for set size: \n"))
r = int(input("Type in r subset size: \n"))

print(f'Your result is {math.factorial(n) / denominator_calc(n, r)}')
