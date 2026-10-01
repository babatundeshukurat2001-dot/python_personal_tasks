x = [[0] * 4 for _ in range(4)] 
 
x[0][0] = x[0][3] = x[3][0] = x[3][3] = 1

for row in x:

    print(row)
