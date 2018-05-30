import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(123)
#e = np.random.standard_t(df = 100000, size = 100000)
theta = 0.6

e = pd.read_csv('y.csv')
e = np.array(e['x'])

def T(n):
    t = [1]
    tmp = 1
    for i in range(n):
        tmp = theta * tmp + e[i]
        t.append(tmp)
    return t

t = [T(x) for x in [100,1000,10000,100000]]

x = list(range(101))
y = t[0]
plt.plot(x,y)
plt.show()

def sd(x):
    m = 0
    b = (1 - theta ** 2) ** -1
    a = -0.5 * ((x - m) ** 2) / b
    c = 1 / np.sqrt(2 * np.pi * b)
    return c * np.exp(a)

x = np.arange(-5,5,0.1)

a = sum(t[3]) / (100001)
print(a)
b = sum([x**2 for x in t[3][1:]]) / 100000
print(b)

print((1 - theta ** 2) ** -1)

#折れ線グラフ、ヒストグラム、正規分布のグラフ
for i in range(4):
    plt.subplot(221 + i)
    plt.hist(t[i],normed=True,bins=100)
    y = [sd(z) for z in x]
    plt.plot(x,y)
plt.show()
