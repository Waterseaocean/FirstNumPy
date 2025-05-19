import numpy as np

x_1 = np.array(
    [1, 2, 3]
)
x_2 = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)
x_3 = np.array(
    [[[1, 2], [3, 4], [5, 6]],
     [[7, 8], [9, 10], [11, 12]]]
)

for x in [x_1, x_2, x_3]:
    print('----')
    print(x.ndim, x.shape)
    print(x)