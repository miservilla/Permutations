import math


def perm_factorial():
    print("This calculates the number of permutations for a given set using the factorial, !n, function.\n")
    result = (math.factorial(int(input("Enter the size of your set as an integer value 'n': \n"))))
    print(f'Your result is {result}.')


def perm_of_subsets():
    print("This calculates the number of permutations for a given set 'n' and subset 'r'.\n")
    n = int(input("Type in 'n': \n"))
    r = int(input("Type in 'r': \n"))
    result = permsubset(n, r)
    print(f'Your result is {result}.')


def permsubset(o, p):
    m = math.factorial(o) / math.factorial(o - p)
    return m


def perm_of_similar_objects():
    print("This calculates the number of permutations for a given set of similar objects, where 'n' is the number of "
          "each similar object.\n")

    numlist = []

    while True:
        n = input("Enter an integer 'n' to continue, or 'Enter' when done: \n")
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


def combinations():
    print("This calculates the number of permutations for a given set 'n' and subset 'r'.\n")

    n = int(input("Type in n for set size: \n"))
    r = int(input("Type in r subset size: \n"))

    print(f'Your result is {math.factorial(n) / denominator_calc_for_combinations(n, r)}')


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


def denominator_calc_for_combinations(o, p):
    return math.factorial(p) * math.factorial(o - p)


# Program starts here.

while True:
    selection = input("Select:\n0. for 'Permutations'\n1. for 'Permutations of Subsets'\n2. for 'Permutation of "
                      "Similar Objects'\n3. for 'Combinations'\n'Enter' to quit: \n")

    if selection.isdigit():
        if int(selection) == 0:
            perm_factorial()
            print("\n")
        elif int(selection) == 1:
            perm_of_subsets()
            print("\n")
        elif int(selection) == 2:
            perm_of_similar_objects()
            print("\n")
        elif int(selection) == 3:
            combinations()
            print("\n")
        else:
            print("Incorrect value!")
            print("\n")
    else:
        break
