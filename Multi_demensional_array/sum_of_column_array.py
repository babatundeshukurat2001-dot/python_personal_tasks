number = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


for count in range(len(number[0])):

        column_sum = 0

        for index in range(len(number):

            column_sum += number[index][count]

        print(f"Column {count}: {column_sum}")

