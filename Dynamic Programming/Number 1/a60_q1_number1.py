def getK(n):
    if n<=1: return 1
    return 2*getK(n//2) + 1

def zeon(k,L,R):
    if k<=1: return k
    c = (getK(k))//2+1
    if L>=c+1:
        return zeon(k//2,L-c,R-c)
    elif R<=c-1:
        return zeon(k//2,L,R)
    elif L==c:
        return k%2 + zeon(k//2,1,R)
    elif R==c:
        return k%2 + zeon(k//2,L,c-1)
    else:
        return zeon(k//2,L,c-1) + k%2 + zeon(k//2,1,R-c)

n,l,r = [int(e) for e in input().strip().split()]
print( zeon(n,l,r) )

