import numpy as np

def arsum(i,j,k):
    if i+k>r or j+k>c: return 0
    s = np.sum(A[i:i+k,j:j+k])
    if s == k**2: return k
    else:
        x = arsum(i+1,j,k)
        if x != 0: return k
        y = arsum(i,j+1,k)
        if y != 0: return k
        z = arsum(i+1,j+1,k)
        return k if z !=0 else 0

r,c = [int(e) for e in input().strip().split()]
A = []
for i in range(r):
    S = []
    for j in input().strip():
        S.append(int(j))
    A.append(S)
A = np.array(A)

for e in range(min(r,c),0,-1):
    k = arsum(0,0,e)
    if k!=0:
        print(k)
        exit()
