from sys import stdin as kb

def cycle(u, G, visited, exceed):
    visited[u] = True
    for v in G[u]:
        if v == exceed: continue
        if visited[v]: return True
        if cycle(v, G, visited, u): return True
    return False

ng = int(kb.readline())
for _ in range(ng):
    n,e = map(int, kb.readline().split())
    gtemp = [set() for _ in range(n)]
    for _ in range(e):
        u,v = map(int, kb.readline().split())
        gtemp[u].add(v)
        gtemp[v].add(u)
    visited = [False]*n
    for i in range(n):
        if not visited[i] and cycle(i, gtemp, visited, -1):
            print("YES")
            break
    else: print("NO")
