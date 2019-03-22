from sys import stdin as kb
import heapq

r,c=map(int,kb.readline().split())
g=[[] for _ in range(r)]
for i in range(r):
    g[i]=[int(e) for e in kb.readline().split()]

d=[[float('inf')]*c for _ in range(r)]
inM=[[False]*c for _ in range(r)]
d[0][0]=0
heap=[(0,0,0)]
heapq.heapify(heap)
while len(heap)>0:
    w,u,v=heapq.heappop(heap)
    inM[u][v]=True
    for x,y in {(0,1),(1,0),(0,-1),(-1,0)}:
        if v+x<c and u+y<r and v+x>=0 and u+y>=0:
            if not inM[u+y][v+x] and d[u+y][v+x] > w+g[u+y][v+x]:
                d[u+y][v+x]=w+g[u+y][v+x]
                heapq.heappush(heap, (d[u+y][v+x], u+y, v+x))

for i in range(r):
    print(*d[i])
