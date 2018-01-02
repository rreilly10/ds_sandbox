"""
Create a 3 x 4 array filled with all zeros, and a 6 x 4 array filled with all 1s.
Concatenate both arrays vertically into a 9 x 4 array, with the all zeros array on top.
Assign the entire first column of the combined array to first_column.
Print out first_column.
"""

import numpy as np

arr = np.zeros((3, 4))
arr2 = np.full((6, 4), 1)

com = np.vstack((arr, arr2))

first_column = com[:, 1]

print(first_column)