'''
0からnまでの積分の近似
nが大きいほど精度が上がる
nを大きくすると、0から∞までの積分の近似になる
(1): integral(1/(1+x)**2)(0->n) = 1 - 1/1+n -> 1
(2): integral(2/1+x**2)(0->n) = 2arctan(n) -> pi
(3): ガウス積分
'''

import math

def I(n, function):
    ans = 0
    for i in range(1, n**2 + 1):
        ans += function(i/n)
    return ans / n

def f1(x):
    return 1 / ((1 + x) ** 2)

def f2(x):
    return 2 / (1 + x ** 2)

def f3(x):
    return math.exp((-1 / 2) * x ** 2)

def f4(x):
    if 0 < x < 1:
        return (x ** 2) * ((1 - x) ** 3)
    else:
        return 0

for j,f in enumerate([f1, f2, f3, f4]):
    print('-----f' + str(j + 1) + '------')
    for i in range(1,5):
        n = 10 ** i
        a = I(n,f)
        print(n)
        print(a)
        if j == 2:
            print(2 * (a ** 2))
