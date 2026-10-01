number = 5

for count in range(number):

    line = ""

    for index in range(number):

        if count == 0 or count == number - 1 or index == 0 or index == number - 1:

            line += "* "

        else:

            line += "  "

    print(line)
