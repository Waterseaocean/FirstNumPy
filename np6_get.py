import numpy as np

# 配列の要素を取得して1次元にまとめる
x = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)

result = x[:, 1] # 行のすべてと２列目の要素を取り出す
print(result)