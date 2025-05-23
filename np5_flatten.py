import numpy as np

# 配列を1次元にする
x = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)

result = x.flatten()
print(result)