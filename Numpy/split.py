import numpy as np

arr = np.array([[10, 20],
                [30, 40],
                [50, 60],
                [70, 80]])

result = np.vsplit(arr, [1, 3])
print(result)