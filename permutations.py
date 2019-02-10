import math
import matplotlib.pyplot as plt
import numpy


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


def combinations(n, r):
    choose = math.factorial(n) / denominator_calc_for_combinations(n, r)
    return choose


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


def mybinomial():
    n = int(input("Type in n for trial size: \n"))
    p = float(input("Type in p for probability: \n"))
    mean = n * p
    var = mean * (1 - p)
    f_sum = 0.0
    f_list = []
    f_dict = {}
    print('Your probability mass function (pmf) results are:\n')
    for i in range(n):
        f = round(combinations(n, i) * (p**i) * (1 - p)**(n - i), 3)
        f_list.append(f)
        f_dict[i + 1] = f
        f_sum += f
        print(f'f({i}) = {f}\n')
    print(f'fsum = {sum(f_list)}\n')
    print(f'mean = {mean}\n')
    print(f'var = {var}\n')
    while True:
        p_range = input("Do you wish to calculate probability range [Y/N]:\n")
        if p_range.upper() == 'Y':
            lower_range = int(input("Enter lower value, lower <= P(X) <= int:\n"))
            upper_range = int(input("Enter upper value, int <= P(X) <= upper:\n"))
            if (lower_range >= 0 or lower_range <= n - 2) and (lower_range < upper_range <= n):
                print(f'P({lower_range} <= X <= {upper_range}) is {round(sum(f_list[lower_range:upper_range + 1]), 3)}')
            else:
                print("Incorrect range values!")
        else:
            break
    p_plot = input("Do you wish to plot pmf [Y/N]:\n")
    if p_plot.upper() == 'Y':
        f_list.insert(0, 0)
        dim = numpy.arange(1, len(f_list), 1)
        ax = plt.subplot(111)
        ax.set_xlim(1, len(f_list) - 1)
        plt.plot(f_list, "o-")
        plt.xticks(dim)
        plt.ylabel("Probability")
        plt.xlabel("f(x) Values of pmf")
        plt.title("Probability Mass Function")
        plt.show()


# Program starts here.


while True:
    selection = input("Select:\n0. for 'Permutations'\n1. for 'Permutations of Subsets'\n2. for 'Permutation of "
                      "Similar Objects'\n3. for 'Combinations'\n4. for 'Binomial (discrete)'\n'Enter' to quit: \n")

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
            print("\nThis calculates the number of permutations for a given set 'n' and subset 'r'.\n")
            n = int(input("Type in n for set size: \n"))
            r = int(input("Type in r subset size: \n"))
            choose = combinations(n, r)
            print(f"Your result is {choose}\n")
        elif int(selection) == 4:
            mybinomial()
            print("\n")
        else:
            print("Incorrect value!")
            print("\n")
    else:
        break
