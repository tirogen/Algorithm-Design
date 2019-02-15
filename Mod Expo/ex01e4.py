def mod(a,n,k):
    if n==1: return a%k
    x = mod(a,n//2,k)
    x *= x
    return x%k if n%2==0 else (x*(a%k))%k
x,n,k=[int(e) for e in input().strip().split()]
print(mod(x,n,k))
