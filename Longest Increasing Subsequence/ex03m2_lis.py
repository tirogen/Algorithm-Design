def lis(c,i):
    if i==n :return 1
    if L[i]>L[c] :return max(1+lis(i,i+1),lis(c,i+1),lis(i,i+1))
    else :return max(lis(c,i+1),lis(i,i+1))


n=int(input().strip())
L=[int(e) for e in input().strip().split()]
#A=[lis(o,o+1) for o in range(n-1)]
print(lis(0,1))

#print(lis(1,1))
