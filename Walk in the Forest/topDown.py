def walk(r,c):
    if r==n-1 and c==m-1: return 0
    if r>n-1 or c>m-1: return float('-inf')
    if mem[r][c]!="d": return mem[r][c]
    right = L[r][c+1] + walk(r,c+1)
    down = L[r+1][c] + walk(r+1,c)
    rido = 2*L[r+1][c+1] + walk(r+1,c+1)
    mem[r][c]=max(right, down, rido)
    return mem[r][c]

n,m=[int(e) for e in input().strip().split()]
mem=[["d"]*(m+1) for e in range(n+1)]
L=[]
for i in range(n):
    L.append([int(o) for o in input().strip().split()]+[float('-inf')])
L+=[[float('-inf')]*(m+1)]
print(L[0][0]+walk(0,0))
