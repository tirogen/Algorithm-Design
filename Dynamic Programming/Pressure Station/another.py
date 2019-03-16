n,k = [int(e) for e in input().strip().split()]
P = [int(e) for e in input().strip().split()]
for i in range(n):
    if i > k:
        print(P[max(0,i-2*k-1):i])
        P[i] += min(P[max(0,i-2*k-1):i])
print(min(P[-k-1:]))
