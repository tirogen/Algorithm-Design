import sys
kb = sys.stdin

def mcsw(i,w):
    store = 0
    high = L[i]
    for k in range(w):
        if i+k>=n: break
        store += L[i+k]
        high = max(store, high)
        if store < 0: break
    return high



n,w = [int(e) for e in kb.readline().strip().split()]
L = [int(e) for e in kb.readline().strip().split()]

print( max([mcsw(i,w) for i in range(n)]) )
