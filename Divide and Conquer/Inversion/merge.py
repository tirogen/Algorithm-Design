def merge(l,r):
    global count
    if l>=r: return A[l:l+1]
    mid = (l+r)//2
    left = merge(l,mid)
    right = merge(mid+1,r)
    for w in left:
        #bad, i am lazy
        count += len([e for e in right if e < w])
    return left+right

n = int(input())
A = [int(e) for e in input().strip().split()]
count = 0
merge(0,n-1)
print(count)
