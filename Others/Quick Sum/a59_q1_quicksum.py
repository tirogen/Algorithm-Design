import sys
kb=sys.stdin

def qsum(r1,c1,r2,c2):
    return p[r2][c2]-p[r1-1][c2]-p[r2][c1-1]+p[r1-1][c1-1]

n,m,k = [int(e) for e in kb.readline().split()]
A=[]
for i in range(n):
    A.append([int(e) for e in kb.readline().split()])
p=[[0]*(m+1) for e in range(n+1)]

p[0][0] = A[0][0]
for j in range(1,m):
    p[0][j] = p[0][j-1]+A[0][j]
for i in range(1,n):
    p[i][0] = p[i-1][0] + A[i][0]
    for j in range(1,m):
        p[i][j] = p[i-1][j] + p[i][j-1]-p[i-1][j-1] + A[i][j]

for i in range(k):
    k = [int(e) for e in kb.readline().split()]
    print(qsum(k[0],k[1],k[2],k[3]))
