n,A = [int(e) for e in input().strip().split()]
N = []
M = [["x"]*(A+1) for e in range(n+1)]
maxLength = int((A-n+1)**0.5)

def tile(i, S):
    if i == n and S > 0: return float('inf')
    elif i == n and S == 0: return 0
    elif S < 0: return float('inf')
    if M[i][S] != "x": return M[i][S]
    M[i][S] = min( [ abs(N[i]-e)**2 + tile(i+1,S-e**2) for e in range(1,maxLength+1) ] )
    return M[i][S]


for i in range(n):
    N.append(int(input()))

ans = tile(0, A)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
