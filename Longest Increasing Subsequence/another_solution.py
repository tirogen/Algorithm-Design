def lic(c,i):
    if i==n:return 1
    if L[i]>L[c]:return max(1+lic(i,i+1), lic(c,i+1))
    else:return lic(c,i+1)

def lis(c,i):
    if i==n :return 0
    if mem[c][i]!="x": return mem[c][i]
    if L[i]>L[c] :
        mem[c][i]=max(1+lic(i,i+1),lis(c,i+1),lis(i,i+1))
    else :
        mem[c][i]=max(lis(c,i+1),lis(i,i+1))
    return mem[c][i]


n=int(input().strip())
L=[int(e) for e in input().strip().split()]
mem=[["x"]*n for e in range(n)]
print(lis(0,1))
