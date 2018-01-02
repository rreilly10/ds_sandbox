import pprint
import csv
import numpy as np

############################
# NATIVE APPROACH
############################

with open("data/winequality-red.csv", "r") as f:

    wines = list(csv.reader(f, delimiter=";"))

    qualities = [float(item[-1]) for item in wines[1:]]

    # print(sum(qualities)/len(qualities))

############################
# NUMPY APPROACH
############################

wines = np.genfromtxt("data/winequality-red.csv", delimiter=";", skip_header=1)
white_wines = np.genfromtxt("data/winequality-white.csv", delimiter=";", skip_header=1)

# COMBINE NUMPY ARRAYS

# Combines all values adding more rows
all_wines = np.vstack((wines, white_wines))
print(all_wines.shape)

# np.hstack combines with columns (adding more data parameters to rows)

# wines[ type of data, element ]

# print(wines[:3, 3])  # First 3 elements from the 4th column
# print(wines[:, 3])  # All of column 4 (residual sugar)
# print(wines[3, :])  # All of row 4

# wines[1, :] = 10
# wines[1, 2] = 10

# third_wine = wines[3, :]
# print(third_wine[1])

# print(wines.astype(np.int))  # Convert np array datatype

# print(wines)
# wines[:, 11] =10  # Adds 10 to all quality scores (ie column 11)
# wines[:, 11] +=10  # Adds 10 to all quality scores (ie column 11) += in place edits
# print(wines)

# classy_drunk = wines[:, 10] * wines[:, 11]  # Multiplies alcahol content by quality
#
# print(classy_drunk)
#
#
# print(wines[:, 11].sum())  # Sum of all quality
# print(wines.sum(axis=0))  # Sum across all columns (shape == 12)
# print(wines.sum(axis=1))  # Sum of each row (shape == number of elements)


# print(wines[:, 11].mean())  # Quality average from before

# Comparison
# print(wines[:, 11] > 5) # Returns a bool array of all wines with a quality above 5
# print(len(wines[:, 11]))

# Subsetting
high_quality = wines[:,11] > 7
# print(wines[high_quality,:][:3,:])

# Advanced Flitering
high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7)
# print(wines[high_quality_and_alcohol,10:])

