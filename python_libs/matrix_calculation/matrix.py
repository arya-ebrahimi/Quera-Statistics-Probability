import numpy as np

# Define A
A = np.array([[1, 2], [5, -2]])

# Define B
B = np.array([[-3, 0], [4, 5]])

# Define C
C = np.array([[4, 25], [-1/2, -3]])

# Define I
I = np.identity(2)

# Calculate C_inv
C_inv = np.linalg.inv(C)

# Calculate D
D = np.dot(A, C_inv)

# Calculate B_T
B_T = B.T

# Calculate M
M = D + B_T + 3*I