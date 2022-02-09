import itertools

if __name__ == '__main__':

    def intersect_sets(lists):
        return list(set.intersection(*map(set, lists.values())))


    def product(x):
        y = x.values()
        product = []
        for x in itertools.product(*y):
            product.append(x)

        return product

    numSets = input("What is the number of sets? (enter an integer): ")

    numSets = int(numSets)

    dictionary = {}

    for x in range(0, numSets):
        a = []

        userInput = input("Input sequence %x with spaces: " % (x + 1))

        for char in userInput:
            if char != ' ':
                a.append(char)

        dictionary["sequence%s" % (x + 1)] = a

    function = input("Cartesian Product of sets or intersection of sets? (C for Cartesian, I for Intersection)")

    function = str(function)

    if (function.lower() == "c"):
        print("Cartesian Product Set is: " + str(product(dictionary)))

    elif (function.lower() == "i"):
        print("Intersection Set is: " + str(intersect_sets(dictionary)))
