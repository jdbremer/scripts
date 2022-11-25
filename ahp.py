import numpy as np
import pandas as pd
# https://towardsdatascience.com/deep-dive-into-analytical-hierarchy-process-using-python-140385fabaa1
# Number of options
n = 3
# Creating default matrix of ones
A = np.ones([n, n])
# Running a for loop to take input from user and populate the upper triangular elements
for i in range(0, n):
    for j in range(0, n):
        if i < j:
            aij = input('How important is option{} over option{} ?: '.format(i, j))
            A[i, j] = float(aij)  # Upper triangular elements
            A[j, i] = 1 / float(aij)  # Lower triangular elements

e = np.linalg.eig(A)[1][:, 0]
p = e / e.sum()


def pairwise_matrix(n):
    A = np.ones([n, n])
    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                aij = input('How important is option{} over option{} ?: '.format(i, j))
                A[i, j] = float(aij)
                A[j, i] = 1 / float(aij)
    # Computing the priority vector
    eig_val = np.linalg.eig(A)[0].max()
    eig_vec = np.linalg.eig(A)[1][:, 0]
    p = eig_vec / eig_vec.sum()
    return p, eig_val


pr_c = pairwise_matrix(3)[0]  # All Criteria
pr_c0 = pairwise_matrix(3)[0]  # Criteria 0: Climate
pr_c1 = pairwise_matrix(3)[0]  # Criteria 1: Sightseeing
pr_c2 = pairwise_matrix(3)[0]  # Criteria 2: Environment

r = pr_c0 * pr_c[0] + pr_c1 * pr_c[1] + pr_c2 * pr_c[2]
print(r)
