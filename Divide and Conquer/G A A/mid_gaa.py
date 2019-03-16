def GAA(n,k):
    if n > mem[k-1]+3+k:
        return GAA(n-mem[k-1]-k-3,k-1)
    elif n > mem[k-1]:
        if n == mem[k-1]+1: return "g"
        else: return "a"
    else:
        return GAA(n, k-1)

n=int(input())
mem = [3]*30
for i in range(1,30):
    mem[i] = 2*mem[i-1]+i+3
print(GAA(n,28))
