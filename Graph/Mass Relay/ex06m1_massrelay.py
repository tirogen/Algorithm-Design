from sys import stdin as kb
from heapq import *

n,m,q=map(int,kb.readline().split())
g=[set() for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,kb.readline().split())
    g[a].add((b,c))
    g[b].add((a,c))

#---- find minimum spaning tree-----
inMST=[False]*n
d=[float('inf')]*n
h=[(0,0)]
d[0]=0
heapify(h)
while len(h)>0:
    du,u=heappop(h)
    inMST[u]=True
    for v,dv in g[u]:
        if not inMST[v] and dv<d[v]:
            d[v]=dv
            heappush(h,(d[v],v))

edge=sorted(d[1:])
for _ in range(q):
    d=int(kb.readline())
    print(max(edge[:n-d]))
