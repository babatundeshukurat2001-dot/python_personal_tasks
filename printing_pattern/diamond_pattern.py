number = 5

for count in range(1, number + 1):

    print(" " * (number - count) + "*" * (2 * count - 1))

    for count in range(number - 1, 0, -1):  

        print(" " * (number - count) + "*" * (2 * count - 1))
