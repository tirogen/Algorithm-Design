import numpy as np

def mod(a,n,k):
    if n==1: return a%k
    x = mod(a,n//2,k)
    x = np.dot(x,x)
    return x%k if n%2==0 else np.dot(x,a%k)%k      
    
n,k = [int(e) for e in input().strip().split()]
A = [int(e) for e in input().strip().split()]
A = np.array([A[0:2], A[2:4]])
A = mod(A,n,k)
B = []
for e in A:
    for o in e:
        B.append(str(o))
print(" ".join(B))
