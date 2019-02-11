n=int(input().strip())
L=[]
for i in range(n):
    x,y=[int(e) for e in input().strip().split()]
    L.append((x,y))
maxY=sorted(L,key=lambda x:-x[1])[0]
count=1
for o in L:
    if o[0]>maxY[0]:count+=1
print(count)
