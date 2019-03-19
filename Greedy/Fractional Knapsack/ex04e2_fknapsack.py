W,n = map(float, input().split())
v = [float(e) for e in input().split()]
w = [float(e) for e in input().split()]
P = sorted([(v[i]/w[i],i) if w[i]!=0 else (float('inf'),i) for i in range(int(n))])[::-1]
M = 0
for f,i in P:
    if W > w[i]:
        M += v[i]
        W -= w[i]
    else:
        M += f*W
        break
print("%.4f"% M)
