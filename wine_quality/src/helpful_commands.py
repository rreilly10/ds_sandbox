import numpy as np

# ALL ZEROS FOR WHEN YOU KNOW A FIXED SIZE BUT
# DON'T HAVE THE DATA YET
empty_array = np.zeros((3, 4))
print(empty_array)


# ALL RANDOM OF A SPECIFIC SIZE
print(np.random.rand(3,4))

array_one = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
)

print(array_one.ravel())