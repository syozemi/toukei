import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
e = np.random.standard_t(df = 10, size = 100)
theta = 0.6

def T(n):
    t = [1]
    tmp = 1
    for i in range(100):
        tmp = theta * tmp + e[i]
        t.append(tmp)
    return t

t = [T(x) for x in [100,1000,10000,100000]]

def sd(x):
    m = 0
    b = (1 - theta ** 2) ** -1
    a = -0.5 * ((x - m) ** 2) / b
    c = 1 / np.sqrt(2 * np.pi * b)
    return c * np.exp(a)

x = list(map(lambda x:x / 10, range(-50,50)))

#折れ線グラフ、ヒストグラム、正規分布のグラフ
for i in range(4):
    plt.subplot(221 + i)
    plt.hist(t[i])
    y = [sd(z) for z in x]
    plt.plot(x,y)
plt.show()
