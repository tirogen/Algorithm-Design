def mergec(l, r):
    global A
    global k
    if l>=r-1 or k<2: return
    mid = (l+r)//2
    A[mid], A[mid-1] = A[mid-1], A[mid]
    k -= 2
    mergec(l,mid)
    mergec(mid,r)

n,k = [int(e) for e in input().strip().split()]
if k%2 == 0:
    print(-1)
    exit()
A = [e for e in range(1,n+1)]
mergec(0,n)
if k == 1:
  print(" ".join([str(e) for e in A]))
else:
  print("-1")
