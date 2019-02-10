def coin(m,L,i):
    if m==0 : return 0
    if i==1 : return m
    if mem[i][m]!="d" : return mem[i][m]
    if m>=L[i]:
        mem[i][m]=min(1+coin(m-L[i],L,i), coin(m,L,i-1))
    else :
        mem[i][m]=coin(m, L, i-1)
    return mem[i][m]

n,m=[int(e) for e in input().strip().split()]
L=[0]+sorted([int(e) for e in input().strip().split()])
mem=[["d"]*(m+1) for e in range(n+1)]
print(coin(m,L,n))
