import numpy as np

r,c = [int(e) for e in input().strip().split()]
A = np.zeros((r+1,c+1))

for i in range(1,r+1):
    j = 1
    for n in input().strip():
        if n == "1":
            A[i][j] = 1+min(A[i][j-1],A[i-1][j],A[i-1][j-1])
        else:
            A[i][j] = 0
        j += 1
print(int(np.max(A)))
