import sys
kb=sys.stdin

mem=[3]*28
def GAA(n):
    if n==0: return 3
    if mem[n]!=3: return mem[n]
    mem[n]= GAA(n-1)+n+3+GAA(n-1)
    return mem[n]
GAA(27)
mem+=[0]

def GA(n, k):
    if mem[k-1]<n<=mem[k-1]+k+3:
        if n==mem[k-1]+1: return "g"
        else: return "a"
    elif n>mem[k]:
        return GA(n, k+1)
    else:
        return GA(n-mem[k-1]-k-3,0)

n=int(kb.readline())
print(GA(n,0))
