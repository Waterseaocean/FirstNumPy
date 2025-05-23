import numpy as np

# 配列・リストで使える関数
x = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)

max = x.max()
print(max)
min = x.min()
print(min)
sum = x.sum()
print(sum)
prod = x.prod() # 要素の積
print(prod)
mean = x.mean() # 平均値
print(mean)
std = x.std() # 標準偏差
print(std)
var = x.var()
print(var)
median = x.median()
print(median)