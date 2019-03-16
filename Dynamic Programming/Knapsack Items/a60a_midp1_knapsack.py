import sys
kb=sys.stdin

n,m=[int(e) for e in kb.readline().strip().split()]
V=[0]+[int(e) for e in kb.readline().strip().split()]
W=[0]+[int(e) for e in kb.readline().strip().split()]
L=[0]*(n+1)
for i in range(n+1):
    L[i]=[int(e) for e in kb.readline().strip().split()]
choose=[]
j=m
for i in range(n,0,-1):
    if L[i][j]-V[i]==L[i-1][j-W[i]]:
        choose.append(i)
        j=j-W[i]
print(str(len(choose))+"\n"+" ".join([str(e) for e in choose]))
