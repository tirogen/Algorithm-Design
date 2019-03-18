n = int(input())
M = [set() for _ in range(n)]
for i in range(n):
    s = [int(e) for e in input().split()]
    for o in s[1:]:
        M[i].add(o)
C = [False]*n
S = []
while len(S) < n:
    for i in range(n):
        if len(M[i])==0 and not C[i]:
            C[i] = True
            S.append(i)
            for L in M:
                L.discard(i)
print(" ".join([str(e) for e in S]))
