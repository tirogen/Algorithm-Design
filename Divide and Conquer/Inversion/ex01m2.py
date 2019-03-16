def part(l,r):
    j = A[l]
    L = [x for x in A[l:r+1] if x < j]
    R = [x for x in A[l:r+1] if x >= j]
    A[l:r+1] = L+R
    return len(L)

def quick(l,r):
    if l>=r: return
    j = part(l,r)
    quick(l,j-1)
    quick(j+1,r)

n = int(input())
A = [int(e) for e in input().strip().split()]

inv(0,n-1)
