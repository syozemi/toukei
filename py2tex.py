import numpy as np

def matrix(a):
    a = np.array(a)
    m,n = a.shape
    s = '\\left(\n\t\\begin{alignedat}{%d}' % n
    se = '\t\\end{alignedat}\n\\right)'
    for i in range(m):
        tmp = ' & '.join(map(str,a[i]))
        if i != m-1:
            s += '\n' + '\t\t' + tmp + '\\\\'
        else:
            s += '\n' + '\t\t' + tmp
    s += '\n' + se
    print(s)


a = np.zeros((4,5))
matrix(a)
