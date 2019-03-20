from sys import stdin as kb
def dfs(u,v,d):
    global dis,ans
    #u is current node
    #v is previous node
    #d is distance
    if dis[u]>-1:
        ans=max(ans,dis[v]-dis[u]+1)
        return
    dis[u]=d
    for o in g[u]:
        if o!=v: dfs(o,u,d+1)

n=int(kb.readline())
g=[set() for _ in range(n)]
for _ in range(n):
    u,v=map(int,kb.readline().split())
    g[u].add(v)
    g[v].add(u)

dis=[-1]*n
ans=0
dfs(0,-1,0)
print(ans)
