import importlib


while True:
    selection = input("Select:\n0. for 'Permutations'\n1. for 'Permutations of Subsets'\n2. for 'Permutation of "
                      "Similar Objects'\n3. for 'Combinations'\n'Enter' to quit: \n")

    if selection.isdigit():
        if int(selection) == 0:
            importlib.import_module('permutation_factorial')
            print("\n")
        elif int(selection) == 1:
            importlib.import_module('permutations_of_subsets')
            print("\n")
        elif int(selection) == 2:
            importlib.import_module('permutation_of_similar_objects')
            print("\n")
        elif int(selection) == 3:
            importlib.import_module('combinations')
            print("\n")
        else:
            print("Incorrect value!")
            print("\n")
    else:
        break
