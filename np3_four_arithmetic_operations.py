import numpy as np

# 行列のすべての要素に対して定数倍にする
x_1 = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)
result1 = x_1 * 3
print("result1")
print(x_1)
print(result1)

# np.array同士の足し算
y_1 = np.array(
    [[10, 20, 30],
     [40, 50, 60]]
)
result2 = x_1 + y_1
print("result2")
print(result2)

# np.dotの計算
x_2 = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)
y_2 = np.array(
    [[10, 20],
     [30, 40],
     [50, 60]]
)
result3 = np.dot(x_2, y_2)
print("result3")
print(result3)

