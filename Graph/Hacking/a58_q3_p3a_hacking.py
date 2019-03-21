from sys import stdin as kb
import heapq

n,m,k=map(int,kb.readline().split())
fhack=[int(e) for e in kb.readline().split()]
c=[int(e) for e in kb.readline().split()]
g=[set() for _ in range(n)]
for _ in range(m):
    u,v=map(int,kb.readline().split())
    g[u].add(v)
    g[v].add(u)

dist=[float('inf')]*n
ans=[0]*n
inMST=[False]*n
heap=[]
for i in fhack:
    dist[i]=c[i]
    ans[i]=c[i]
    heap.append((c[i],i))
heapq.heapify(heap)

while len(heap)>0:
    du,u=heapq.heappop(heap)
    inMST[u]=True
    for v in g[u]:
        if not inMST[v] and dist[v]>du+c[v]:
            dist[v]=du+c[v]
            ans[v]=du+c[v]
            heapq.heappush(heap,(dist[v],v))

print(max(ans))
