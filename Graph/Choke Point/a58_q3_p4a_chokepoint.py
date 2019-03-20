from sys import stdin as kb

def count(u, v):
    global nNode,n
    if u==v: return 0
    c=1
    for o in G[u]:
        if o==v: continue
        tmp=count(o,u)
        nNode[u].append(tmp)
        c+=tmp
    nNode[u].append(n-c)
    return c

def choke(u):
    global nNode
    co = sum(nNode[u])
    for i in range(len(nNode[u])-1):
        for j in range(i+1,len(nNode[u])):
            co += nNode[u][i]*nNode[u][j]
    return co

n = int(kb.readline())
G = [set() for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, kb.readline().split())
    G[u].add(v)
    G[v].add(u)

nNode = [[] for _ in range(n)]
count(0,-1)
for i in range(n): print(choke(i))
