from sys import stdin as kb

n,e,k=map(int,kb.readline().split())
g=[set() for _ in range(n+1)]
for _ in range(e):
    u,v=map(int,kb.readline().split())
    g[u].add(v)
    g[v].add(u)

queue=[(0,0)]
visited=[False]*(n+1)
count=0
while len(queue)>0:
    u,d=queue.pop(0)
    if visited[u]:continue
    visited[u]=True
    if d>k:break
    if d==k:count+=1
    for v in g[u]:
        queue.append((v,d+1))
print(count)
