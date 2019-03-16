from sys import stdin as kb
import bisect as bs

def thanos(L, R):
    global Av,p,k,A,B
    numAv = bs.bisect_right(Av ,R) - bs.bisect_left(Av, L)
    if L == R:
        return B*numAv if numAv > 0 else A
    mid = (L+R)//2
    destroyAll = B*numAv*(R-L+1) if numAv > 0 else A
    destroyLR = thanos(L, mid) + thanos(mid+1,R)
    return min(destroyAll,destroyLR)

p,k,A,B = [int(e) for e in kb.readline().split()]
Av = sorted([int(e) for e in kb.readline().split()])
print(thanos(1,pow(2,p)))
