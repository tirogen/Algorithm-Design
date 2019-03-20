from sys import stdin as kb
import bisect as bs

def thanos(L,R,A,B):
    if L>R: return 0
    mid = (L+R)//2
    numAv=bs.bisect_right(Av,R)-bs.bisect_left(Av,L)
    destroyAll = B*numAv*(R-L+1) if numAv>0 else A
    if L==R or numAv==0: return destroyAll
    destroyLR = thanos(L,mid,A,B)+thanos(mid+1,R,A,B)
    return min(destroyAll,destroyLR)

p,k,A,B = [int(e) for e in kb.readline().split()]
Av = sorted([int(e) for e in kb.readline().split()])
print(thanos(1,pow(2,p),A,B))
