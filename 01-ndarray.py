import torch

print(dir(torch.distributions))

x = torch.arange(12)

print(x)

print(x.shape)

X = x.reshape(3, 4)
print(X)

torch.zeros(2, 3, 4)

# 张量运算
y = torch.tensor([1.0, 2, 4, 8])
# e的y次方
print(torch.exp(y))

# 张量连结，dim = 0 按行连接
X = torch.arange(12, dtype=torch.float32).reshape(3, 4)
Y = torch.tensor([[2.0, 1, 3, 4], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((X, Y), dim=0))

# 张量元素求和
print(X.sum())

# 张量求和（广播机制）两个不同形状的矩阵，内部复制为形状相同
print(X + Y)

# 张量索引 : 左闭右开
print(X[-1])
print(X[1:3])

print(X[1, 2])

# 原地操作
Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X + Y
print('id(Z):', id(Z))



