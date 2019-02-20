n,k = [int(e) for e in input().strip().split()]
P = [int(e) for e in input().strip().split()]
M = [[float('inf')]*(4*k+1) for o in range(n)]
for j in range(2*k+1):
    if j > k:
        M[n-1][j] = 0
    else:
        M[n-1][j] = P[n-1]
for i in range(n-2,-1,-1):
    for j in range(2*k+1):
        if j == 0:
            M[i][j] = P[i] + M[i+1][2*k]
        else:
            M[i][j] = min(P[i]+M[i+1][2*k], M[i+1][j-1])
print(M[0][k])
