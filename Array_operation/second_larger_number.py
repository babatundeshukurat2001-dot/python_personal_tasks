number = [5, -3, 8, 2, -7, 8, 10, 1]

first = second = None

for count in number:

    if first is None or count > first:

        second = first

        first = count

    elif count != first and (second is None or count > second):

        second = count

print(second)
