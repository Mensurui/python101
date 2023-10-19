# Define a sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
vectors = [
    [1],
    [2],
    [3]
]

# Iterate through rows of the matrix
for row in matrix:
    for element in row:
        print(element, end=' ')  # Use end=' ' to print elements on the same line
    print()  # Move to the next line for the next row

print("_____________________")
print()

# Iterate through vectors
for vector in vectors:
    for element in vector:
        print(element, end=' ')
    print()

print("_____________________")
print()

# Perform element-wise multiplication

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result = matrix[j][i] * vectors[i][0]
        print(result, end=' ')
    print()
