def pres(i,j):
    if i == n-1:
        if j <= k: return P[i]
        else: return 0
    if M[i][j] != "x": return M[i][j]
    if j == 0: return P[i]+pres(i+1,2*k)
    M[i][j] = min(P[i]+pres(i+1,2*k), pres(i+1,j-1))
    return M[i][j]

n,k = [int(e) for e in input().strip().split()]
P = [int(e) for e in input().strip().split()]
M = [["x"]*(2*k+1) for i in range(n+1)]
print( pres(0,k) )
