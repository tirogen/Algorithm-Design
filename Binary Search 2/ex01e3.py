def bsn(l,r,x):
    if l<0 or r>n-1: return -1
    mid=(l+r)//2
    if N[mid]>x: return bsn(l,mid-1,x)
    elif N[mid]<x: return bsn(mid+1,r,x)
    elif N[mid]==x: return mid

n,m=[int(e) for e in input().strip().split()]
N=[int(e) for e in input().strip().split()]

print(  bsn(0,n-1,9 ) )
