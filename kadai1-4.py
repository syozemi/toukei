import numpy as np
import matplotlib.pyplot as plt

def eigenvalue(n):
    X = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            if i == j:
                X[i][j] = np.random.normal(0,2)
            else:
                tmp = np.random.normal(0,1)
                X[i][j] = tmp
                X[j][i] = tmp
    X = X / (n ** 0.5)
    eig = np.linalg.eig(X)
    return list(eig[0].real)

def f(x):
    return (4 - x ** 2) ** 0.5 * 0.5 / np.pi

l = []
for _ in range(1000):
    l = l + eigenvalue(100)
plt.hist(l, normed=True, bins=100)

x = np.arange(-2,2,0.01)
y = f(x)
plt.plot(x,y)

plt.show()