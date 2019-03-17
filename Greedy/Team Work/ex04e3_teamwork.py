n,m = map(int, input().split())
s = sorted([int(e) for e in input().split()])
S = [[] for _ in range(n)]
R = [[] for _ in range(n)]
i = 0
for t in s:
    S[i%n].append(t)
    i += 1

for b in range(n):
    z = 0
    for a in S[b]:
        z += a
        R[b].append(z)

z = sum([sum(x) for x in R])/m
print("%.3f"%z)
