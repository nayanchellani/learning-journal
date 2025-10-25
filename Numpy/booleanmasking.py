import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Fancy indexing
fancy = arr[[1, 3, 4]]

# Boolean masking
mask = arr[arr > 25]
print(mask)