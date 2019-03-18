from sys import stdin as kb

def order(u):
    global visited,GT,orders
    if visited[u]: return
    visited[u] = True
    for v in GT[u]: order(v)
    orders.append(u)

def dfs(u, l):
    global visited, G
    if visited[u]: return
    visited[u] = True
    l.append(u)
    for v in G[u]: dfs(v, l)

n = int(kb.readline())
G = [[] for _ in range(n)]
GT = [[] for _ in range(n)]
for i in range(n):
    s = [int(e) for e in kb.readline().split()]
    for v in s[1:]:
        G[i].append(v)
        GT[v].append(i)
visited, orders = [False]*n, []
for i in range(n): order(i)

scc = []
visited = [False]*n
while sum(scc) < n:
    index = orders.pop(-1)
    tmp = []
    dfs(index, tmp)
    scc.append(len(tmp))

print(" ".join([str(e) for e in sorted(scc) if e!=0]))

