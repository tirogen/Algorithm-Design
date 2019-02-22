def mergec(l, r):
    global A
    global k
    if l>=r-1 or k<=0: return
    mid = (l+r)//2
    tmp = A[mid]
    A[mid] = A[mid-1]
    A[mid-1] = tmp
    k -= 2
    if k<=0: return
    mergec(l,mid)
    mergec(mid,r)


n,k = [int(e) for e in input().strip().split()]
if k%2 == 0:
    print(-1)
    exit()
A = [e for e in range(n)]
k -= 1
mergec(0,n)
print(" ".join([str(e) for e in A]))
