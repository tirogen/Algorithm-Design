from sys import stdin as kb

n,e=map(int,kb.readline().split())
gt=[set() for _ in range(n+1)]
for _ in range(e):
    u,v=map(int,kb.readline().split())
    gt[v].add(u)

for _ in range(5):
    done = set()
    for s in [int(e) for e in kb.readline().split()]:
        isBreak = False
        for o in gt[s]:
            if o not in done:
                print("FAIL")
                isBreak = True
                break
        if isBreak: break
        done.add(s)
    else:
        print("SUCCESS")
