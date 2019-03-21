from sys import stdin as kb

n,e,s=map(int,kb.readline().split())
g=[set() for _ in range(n)]
for _ in range(e):
    a,b,w=map(int,kb.readline().split())
    g[a].add((b,w))

d=[float('inf')]*n

d[s]=0
for _ in range(n+1):
    relax=False
    for u in range(n):
        for v,w in g[u]:
            if d[v]>w+d[u]:
                d[v]=w+d[u]
                relax=True
if relax:print(-1)
else:print(*d)
