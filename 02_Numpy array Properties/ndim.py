import numpy as np

array_1d = np.array([1,2,3,4])

array_2d = np.array([[1,2,3],
                     [3,4,5],
                     [6,7,8]])

array_3d = np.array([[[1,2],[2,3],[3,4],[4,5]]])

print(array_1d.ndim)
print(array_2d.ndim)
print(array_3d.ndim)