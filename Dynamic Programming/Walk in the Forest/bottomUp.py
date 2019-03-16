n,m = [int(e) for e in input().strip().split()]
L = []
M = [[0]*m for e in range(n)]
for i in range(n):
    L+=[[int(e) for e in input().strip().split()]]
M[0][0] = L[0][0]
for i in range(1,n):
    M[i][0] = L[i][0] + M[i-1][0]
for j in range(1,m):
    M[0][j] = L[0][j] + M[0][j-1]
for i in range(1,n):
    for j in range(1,m):
        right = L[i][j]+M[i][j-1]
        down = L[i][j]+M[i-1][j]
        dori = 2*L[i][j]+M[i-1][j-1]
        M[i][j] = max(right, down, dori)
print(M[n-1][m-1])
