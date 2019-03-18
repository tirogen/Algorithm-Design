from sys import stdin as kb

n, e, k = map(int, kb.readline().split())
G = [set() for _ in range(n)]
for _ in range(e):
    u,v = map(int, kb.readline().split())
    G[u].add(v)
    G[v].add(u)

maxC = 0
for i in range(n):
    visited = [False]*n
    visited[i], q = True, [(i, 0)]
    count = 0
    while len(q)>0:
        u, d = q.pop(0)
        if d > k: break
        count += 1
        for v in G[u]:
            if v == u: continue
            if not visited[v]:
                visited[v] = True
                q.append((v, d+1))
    maxC = max(maxC, count)

print(maxC)
