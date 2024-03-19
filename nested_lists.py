matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)

print("#####################################################################")

first_row_first_column = matrix[0][0]
print(first_row_first_column)

print("#####################################################################")

for row in matrix:
    print(row)

print("#####################################################################")

for row in matrix:
    print('m'.join(map(str, row)))