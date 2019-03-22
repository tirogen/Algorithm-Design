from sys import stdin as kb
import heapq

r,c=map(int,kb.readline().split())
g=[]
for _ in range(r):
    g.append(kb.readline().strip())

d=[[float('inf')]*c for _ in range(r)]
d[0][0]=0
q=[(0,0,0)]
heapq.heapify(q)
while len(q)>0:
    du,a,b=heapq.heappop(q)
    for x,y in {(0,1),(1,0),(-1,0),(0,-1)}:
        if 0<=a+x<c and 0<=b+y<r and du+1<d[b+y][a+x] and g[b+y][a+x]==".":
            d[b+y][a+x]=du+1
            heapq.heappush(q,(d[b+y][a+x],a+x,b+y))
if d[r-1][c-1]==float('inf'): print(-1)
else:print(d[r-1][c-1])
