import numpy as np
from scipy import linalg


#a) Define a matrix A
A = np.arange(1, 10).reshape(3, 3)

#b) Define a vector b
b = np.arange(1, 4)

#c) Solve the linear system of equations A x = b
x = linalg.solve(A, b)

#d) Check that your solution is correct by plugging it into the equation
A.dot(x.T)

#e) Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)

# Generate random matrix
B = np.random.rand(9).reshape(3, 3)
print(B)

# Solve for x
X = linalg.solve(A, B)

np.dot(A, X)
