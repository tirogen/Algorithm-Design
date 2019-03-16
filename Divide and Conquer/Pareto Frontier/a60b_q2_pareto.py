import sys
kb=sys.stdin
def pareto(l,r):
    if l>r: return
    if l==r: return L[l:l+1]
    m=(l+r)//2
    left = pareto(l,m)
    right = pareto(m+1,r)
    maxYR = sorted(right,key=lambda x:-x[1])[0]
    newLeft = [e for e in left if e[1]>maxYR[1]]
    return newLeft+right
    
n=int(kb.readline())
L=[]
for i in range(n):
    L.append([int(e) for e in kb.readline().strip().split()])
L.sort()
print(len(pareto(0,n-1)))
