mem=[[0]*31 for e in range(31)]
def C(n,k):
    if n==k or k==0: return 1
    if mem[n][k]!=0:return mem[n][k]
    mem[n][k]=C(n-1,k-1)+C(n-1,k)
    return mem[n][k]
n,k=[int(e) for e in input().strip().split()]
print(C(n,k))
