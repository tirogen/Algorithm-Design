import sys
kb=sys.stdin

n=int(kb.readline())
L=[]
for i in range(n):
    store=[int(e) for e in input().strip().split()]
    L.append(store)
daw=["x"]*n

for i in range(n):
    if daw[i]=="x":
        for j in range(n):
            isBreak = False
            if L[i][j]==1 and i!=j:
                daw[i]=False
                isBreak=True
            if L[j][i]==1 and i!=j:
                daw[j]=False
            if isBreak: break
        else:
            for k in range(n):
              if L[k][i]==0 and i!=k:
                  daw[i]=False
                  break
            else:
                daw[i]=True
for i in range(n):
    if daw[i]:
        print(i+1)
        break
else:
    print(0)
