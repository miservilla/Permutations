import math


def numerator_calc(numlistnum):
    o: int = 0
    for num in numlistnum:
        o += num
    o = math.factorial(o)
    return o


def denominator_calc(numlistden):
    p: int = 1
    for num in numlistden:
        p *= math.factorial(num)
    return p


print("This calculates the number of permutations for a given set of similar objects, where 'n' is the number of "
      "each similar object.\n")

numlist = []

while True:
    n = input("Enter an integer 'n' to continue, or 'Enter' when done: ")
    if n.isdigit():
        numlist.append(int(n))
    else:
        break

if len(numlist) == 0:
    print("List is empty!")
else:
    numerator = numerator_calc(numlist)
    denominator = denominator_calc(numlist)

    print(f'The list you entered is {numlist}.')
    print(f'Your result is {numerator / denominator}.')
