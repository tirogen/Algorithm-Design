import numpy as np

def lis(i,j):
    global n,M
    if i >= n: return 0
    if M[i][j]!="x": return M[i][j]
    if L[i]>j:
        M[i][j] = max(1+lis(i+1,L[i]), lis(i+1,j))
    else:
        M[i][j] = lis(i+1,j)
    return M[i][j]

n = int(input().strip())
L = np.zeros(n, dtype=np.int32)
i = 0
for e in input().strip().split():
    L[i] = int(e)
    i += 1
M = [["x"]*(np.max(L)+5) for i in range(n+5)]
print( max([lis(i,-1) for i in range(n)]) )
