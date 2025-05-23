import numpy as np

# 配列の形を変形
x = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)

result = x.reshape(3, 2)
print(result)