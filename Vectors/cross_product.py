# Input vectors in three-dimensional space
a = input("Input the first vector in three-dimensional space (e.g., 1 2 3): ").split()
b = input("Input the second vector in three-dimensional space (e.g., 4 5 6): ").split()

# Check if both input lists have exactly three elements
if len(a) != 3 or len(b) != 3:
    print("Both vectors must be three-dimensional.")
else:
    # Convert the input strings to floats
    a = [float(x) for x in a]
    b = [float(x) for x in b]

    # Calculate the cross product
    crossproduct = [a[1]*b[2] - b[1]*a[2], a[2]*b[0] - b[2]*a[0], a[0]*b[1] - b[0]*a[1]]
    print("The cross product of the two vectors is:", crossproduct)
