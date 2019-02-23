def getQ(t):
    T = 0
    for i in N:
        T += t//i
    return T+n

def getT(x, l, r):
    mid = (l+r)//2
    if l >= r: return l
    canServe = getQ(mid)
    if x == canServe:
        tt = mid
        while True:
            tt -= 1
            can = getQ(tt)
            if can != canServe:
                return tt+1
    elif x > canServe: return getT(x, mid+1, r)
    else: return getT(x, l, mid)

n,a = [int(e) for e in input().strip().split()]
N = [int(e) for e in input().strip().split()]
A = [int(e) for e in input().strip().split()]

for c in A:
    print(getT(c, 0, 1000000000000))
