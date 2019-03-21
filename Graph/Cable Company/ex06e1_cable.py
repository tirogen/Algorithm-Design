from sys import stdin as kb
import numpy as np

n=int(kb.readline())
g=[[0]*n for _ in range(n)]
for i in range(n-1):
    cost=[int(e) for e in kb.readline().split()]
    t=0
    for j in range(i+1,n):
       g[i][j]=cost[t]
       g[j][i]=cost[t]
       t+=1
        
d=[float('inf')]*n
inMST=[False]*n
d[0]=0
ans=[0]*n
for _ in range(n):
    u=np.argmin(d)
    d[u]=float('inf')
    inMST[u]=True
    for v in range(n):
        if not inMST[v] and g[u][v]<d[v]:
            d[v]=g[u][v]
            ans[v]=g[u][v]
print(sum(ans))
