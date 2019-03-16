n = int(input())
s = [int(e) for e in input().split()]
f = [int(e) for e in input().split()]
s = sorted([(f[i], s[i]) for i in range(n)])
count = 0
finish = 0
for e in s:
    if e[1] >= finish:
        count += 1
        finish = e[0]
print(count)
