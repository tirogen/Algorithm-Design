def sure(i):
    if i>=n: return 1
    s1=P[i]+pres(i+1)
    s2=P[i]+pres(i+2)
    s3=P[i]+pres(i+3)
    return min(s1,s2,s3)

def pres(i):
    if i>=n: return 1
    x1=P[i]+pres(i+1)
    x2=P[i]+pres(i+2)
    x3=P[i]+pres(i+3)
    x4=P[i]+pres(i+4)
    x5=P[i]+pres(i+5)
    x6=P[i]+pres(i+6)
    x7=sure(i+3)
    return min(x1,x2,x3,x4,x5,x6,x7)

n,k = [int(e) for e in input().strip().split()]
P = [int(e) for e in input().strip().split()]
Mi = [(e,P[e]) for e in range(n)]+[(0,0)]
x = pres(0)
print(x)
