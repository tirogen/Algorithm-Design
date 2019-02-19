def diagsum(r,c):
    if r==n-1 or c==n-1: return L[r][c]
    if MEM[r][c]!="x": return MEM[r][c]
    MEM[r][c] = max(L[r][c]+diagsum(r+1,c+1), L[r][c])
    return MEM[r][c]

n=int(input().strip())
L=[]
MEM=[["x"]*n for i in range(n)]
for e in range(n):
    L.append([int(e) for e in input().strip().split()])
print(max([diagsum(i,j) for i in range(n) for j in range(n)]))
