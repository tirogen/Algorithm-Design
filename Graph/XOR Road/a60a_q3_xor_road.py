from sys import stdin as kb
import numpy as np

n=int(kb.readline())
N=[]
for _ in range(n):
    N.append(int(kb.readline()))

dist=[0]*n
ans=[0]*n
inMST=[False]*n
for _ in range(n):
    u=np.argmax(dist)
    dist[u]=0
    inMST[u]=True
    for v in range(n):
        if v==u:continue
        if not inMST[v] and dist[v]<(N[u]^N[v]):
            tmp=N[u]^N[v]
            dist[v]=tmp
            ans[v]=tmp
print(sum(ans))
