import sys
kb = sys.stdin
sys.setrecursionlimit(5000)

def order(u):
    global GT,orders,visited
    if visited[u]: return
    visited[u] = True
    for v in GT[u]:
        order(v)
    orders.append(u)

def dfs(u, tmp):
    global G,visited
    if visited[u]: return
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            tmp.append(v)
            dfs(v, tmp)

def getHeight(u, d):
    global height, GT
    if height[u] >= d: return
    height[u] = d
    for v in GT[u]:
        getHeight(v, d+1)


#-------- input zone -------------------
n,p = map(int, kb.readline().split())
G = [set() for _ in range(n)]
GT = [set() for _ in range(n)]
for _ in range(p):
    u,v = map(int, kb.readline().split())
    G[u].add(v)
    GT[v].add(u)
#---------------------------------------


#--------strongly connected component---
orders = []
visited = [False]*n
for i in range(n): order(i)
scc = []
comp = [-1]*n
visited = [False]*n
while len(orders) > 0:
    u = orders.pop(-1)
    if visited[u]: continue
    tmp = [u]
    dfs(u, tmp)
    c = len(scc)
    for v in tmp:
        comp[v] = c
    scc.append(tmp)
#-----------------------------------------


#--------combination scc to node----------
GT = [set() for _ in range(len(scc))]
for i in range(len(scc)):
    for u in scc[i]:
        for v in G[u]:
            if comp[v]!=i:
                GT[i].add(comp[v])
#-----------------------------------------


#-------get height of graph---------------
orders = []
visited = [False]*len(scc)
for i in range(len(scc)): order(i)
height = [-1]*len(scc)
while len(orders) > 0:
    u = orders.pop(-1)
    if height[u] > -1: continue
    getHeight(u, 0)
#-----------------------------------------


#-------solve------------------------------
height = sorted([(height[i], i) for i in range(len(height))])
solution = [0]*n
for h,i in height:
    solution[h] += len(scc[i])
print(*[s for s in solution if s!=0])
