import numpy as np

np.random.seed(137)
x = np.random.randn(6)

#create matrix A (not elegant, needs better code)
a = np.zeros((4,4))
a[0,1] = x[0]
a[1,0] = -1 * x[0]
a[0,2] = x[1]
a[2,0] = -1 * x[1]
a[0,3] = x[2]
a[3,0] = -1 * x[2]
a[1,2] = x[3]
a[2,1] = -1 * x[3]
a[1,3] = x[4]
a[3,1] = -1 * x[4]
a[2,3] = x[5]
a[3,2] = -1 * x[5]

#create matrix B
b = np.identity(4)
n = 1
a_ = np.identity(4)
for i in range(1,101):
    n = n * i
    a_ = np.matmul(a_, a)
    b = np.add(b, a_ / n)
b = b.astype(np.float64)

#print(a)
#print(b)

detA = np.linalg.det(a)
detB = np.linalg.det(b)
#print(detA)
#print(detB)

eigA = np.linalg.eig(a)
eigB = np.linalg.eig(b)








