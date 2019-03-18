import numpy as np
W,n = map(np.float64, input().split())
v = [np.float64(e) for e in input().split()]
w = [np.float64(e) for e in input().split()]
P = sorted([(np.divide(v[i],w[i],dtype=np.float64),i) for i in range(int(n))])[::-1]
M = 0
for f,i in P:
    if W > w[i]:
        M += v[i]
        W -= w[i]
    else:
        M += f*W
        break
print("%.4f"% M)
