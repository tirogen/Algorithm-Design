n = int(input())
S = sorted([int(e) for e in input().strip().split()])
if S[0] < 1 or S[-1] > n:
    print("NO")
    exit()
for i in range(n-1):
    if S[i] == S[i+1]:
        print("NO")
        break
else:
    print("YES")
