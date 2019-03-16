def D(n,k):
    if n<k: return 0
    if k==1: return 1
    if M[n][k]!="x": return M[n][k]
    M[n][k] = (((D(n-1,k)%1997)*(k%1997))%1997 + D(n-1,k-1)%1997)%1997
    return M[n][k]

n,k = [int(e) for e in input().strip().split()]
M = [["x"]*(k+1) for i in range(n+1)]
print(D(n,k))
