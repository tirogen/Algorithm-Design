from bisect import *

def date(k):
    global p,d
    peak = 0
    for t in range(d):
        tmp = bisect_right(p, peak+k)
        if tmp == 0: continue
        peak = p[tmp-1]
        if peak >= p[-1]:
            return t+1
    return d+1

def search(kL ,kR):
    global d
    if kL >= kR: return kL
    mid = (kL+kR)//2
    return search(kL, mid) if date(mid) <= d else search(mid+1, kR)

n,d = map(int, input().split())
p = [int(e) for e in input().split()]
k = search(p[-1]//d-1, p[-1])
print(k, date(k))
