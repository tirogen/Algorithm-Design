def bs(l,r,x):
    while l<r and r>l:
        mid=(l+r)//2
        print(l,r,mid)
        if L[mid]==x and L[mid+1]==x:
            l=mid+1
        elif L[mid]==x and L[mid+1]>x:
            return mid
        elif L[mid]>x:
            r=mid
        elif L[mid]<x:
            l=mid+1
    return -1 if min(L)>x else n-1


n,m=[int(e) for e in input().strip().split()]
L=[int(e) for e in input().strip().split()]
M=[int(e) for e in input().strip().split()]
print(bs(0,n-1,11))
##for e in M: 11
##    print(bs(0,n-1,e))
