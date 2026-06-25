import numpy as np

# Create two 2D matrices
A = np.array([[1, 2, 3],[4, 5, 6]])

B = np.array([[7, 8, 9],[1, 2, 3]])

print("Matrix A:", A)
print("Matrix B:", B)

# Addition
print("\nAddition of matrices:", A + B)

# Subtraction
print("\nSubtraction of matrices", A - B)

# Element-wise multiplication
print("\nElement-wise multiplication", A * B)

# Transpose
print("\nTranspose of Matrix A:", A.T)

# Matrix multiplication
print("\nMatrix multiplication:\n", np.dot(A, B.T))
