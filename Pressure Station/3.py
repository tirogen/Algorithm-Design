def pres(i, left):
    if i>=n: return
    if left==0:
        return P[i]+pres(i+1, 2*k)
    else:
        #2 sure
        m1=P[i]+pres(i+1, left)
        m2=P[i]+pres(i+2, left-1)
        m3=P[i]+pres(i+3, left-2)
        m4=pres(i+1, left-2)
        return min(m1, m2, m3, m4)

n,k = [int(e) for e in input().strip().split()]
P = [int(e) for e in input().strip().split()]
Mi = [(e,P[e]) for e in range(n)]+[(0,0)]
x = pres(0, 2*k)
print(x)
