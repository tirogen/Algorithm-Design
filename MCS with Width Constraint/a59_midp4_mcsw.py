import sys
import numpy as np
kb = sys.stdin

n,w = [int(e) for e in kb.readline().strip().split()]
L = np.zeros(n, dtype=np.int32)
i = 0
for e in kb.readline().strip().split():
    L[i] = int(e)
    i += 1

M = max(L)
##for i in range(n):
##    zum = 0
##    for k in range(w):
##        if i+k < n: zum += L[i+k]
##        M = max(M, zum)
##        if zum < 0:
##            i = i+k
##            break

i = 0
while i < n:
    zum = 0
    for k in range(w):
        if i+k < n: zum += L[i+k]
        M = max(M, zum)
        if zum < 0: break
    i += k+1
print(M)
