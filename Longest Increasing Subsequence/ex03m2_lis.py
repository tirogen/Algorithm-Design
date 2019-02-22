n = int(input().strip())
L = [int(e) for e in input().strip().split()]
A = [1]*n
for i in range(1,n):
    for j in range(i):
        if L[i] > L[j]:
            A[i] = max(A[i], A[j]+1)
print(max(A))

