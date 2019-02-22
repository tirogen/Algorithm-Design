n,m = [int(e) for e in input().strip().split()]
L = []
M = [[0]*m for e in range(n)]
for i in range(n):
    L+=[[int(e) for e in input().strip().split()]]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            M[i][j] = L[i][j]
        else:
            if j>0:
                left = L[i][j] + M[i][j-1]
            else:
                left = float('-inf')
            if i>0:
                up = L[i][j] + M[i-1][j]
            else:
                up = float('-inf')
            if i>0 and j>0:
                uple = 2*L[i][j] + M[i-1][j-1]
            else:
                uple = float('-inf')
            M[i][j] = max(up,left,uple)
print(M[n-1][m-1])
