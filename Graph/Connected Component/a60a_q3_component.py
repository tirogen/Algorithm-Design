import sys
kb=sys.stdin
sys.setrecursionlimit(5000)

def order(u):
    if visited[u]:return
    visited[u]=True
    for v in g[u]:order(v)
    orders.append(u)

def dfs(u):
    if visited[u]:return
    visited[u]=True
    for v in g[u]:dfs(v)

n,e=map(int,kb.readline().split())
g=[set() for _ in range(n+1)]
for _ in range(e):
    u,v=map(int,kb.readline().split())
    g[u].add(v)
    g[v].add(u)

orders=[]
visited=[False]*(n+1)
for i in range(1,n+1):order(i)

visited=[False]*(n+1)
count=0
while len(orders)>0:
    u=orders.pop(-1)
    if visited[u]:continue
    dfs(u)
    count+=1
print(count)
