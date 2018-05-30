import numpy as np
import cmath
import matplotlib.pyplot as plt

#create matrix A

x = [0.3835199,  1.3669469, -0.3452020,  1.3491541,  0.3029958,  0.5207242]

a = np.array([
    [0, x[0], x[1], x[2]],
    [-x[0], 0, x[3], x[4]],
    [-x[1], -x[3], 0, x[5]],
    [-x[2], -x[4], -x[5], 0]
    ])

#difs = []

#create matrix B
b = np.identity(4)
n = 1
a_ = np.identity(4)
for i in range(1,101):
    n = n * i
    a_ = np.matmul(a, a_)
    b = np.add(b, a_ / n)
    '''if i == 100:
        print(a_)'''
    b = b.astype(np.float64)
    '''detA = np.linalg.det(a)
    detB = np.linalg.det(b)
    eigA = np.linalg.eig(a)
    eigB = np.linalg.eig(b)
    expA = [cmath.exp(x) for x in eigA[0]]
    dif = 0
    for i in range(4):
        dif += abs(expA[i] - eigB[0][i])
    difs.append(dif)'''

detA = np.linalg.det(a)
detB = np.linalg.det(b)

eigA = np.linalg.eig(a)
eigB = np.linalg.eig(b)

expA = [cmath.exp(x) for x in eigA[0]]

print('A')
print(a)
print('B')
print(b)
print('')
print('detA')
print(detA)
print('detB')
print(detB)
print('')
print('=== A ===')
print(eigA[0])
print('---------')
print(eigA[1].T)
print('=== B ===')
print(eigB[0])
print('---------')
print(eigB[1].T)
print('')
print(expA)
'''
x = list(range(1,101))
y = difs
plt.plot(x,y)
plt.xlabel('m')
plt.ylabel('d')
plt.show()
'''