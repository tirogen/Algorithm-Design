from sys import stdin as kb
from collections import deque

def bfs(R,C,mapp,mon,end):
    d=[[float('inf')]*C for _ in range(R)]
    q=deque()
    for o in mon:
        d[o[1]][o[2]]=o[0]
        q.append(o)
    while len(q)>0:
        du,y,x=q.popleft()
        for a,b in {(0,1),(1,0),(-1,0),(0,-1)}:
            if 0<=y+a<R and 0<=x+b<C and mapp[y+a][x+b]=="."\
               and du+1<d[y+a][x+b] and du+1<=end:
                d[y+a][x+b]=du+1
                q.append((d[y+a][x+b],y+a,x+b))
    return d

for _ in range(int(kb.readline())):
    R,C,n,T,r,c=map(int,kb.readline().split())
    ghosts=set()
    for _ in range(n):ghosts.add(tuple(map(int,kb.readline().split())))
    mapp=[]
    for _ in range(R):mapp.append(kb.readline().strip())

    pacmanMap=bfs(R,C,mapp,{(0,r,c)},T)
    ghostsMap=bfs(R,C,mapp,ghosts,T)

    for i in range(R):
        for j in range(C):
            if ghostsMap[i][j]==float('inf') and pacmanMap[i][j]<=T:
                print("YES")
                break
        else:continue
        break
    else:print("NO")
