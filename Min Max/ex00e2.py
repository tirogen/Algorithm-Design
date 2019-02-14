n,m=[int(e) for e in input().strip().split()]
r=int(input().strip())
matrix=[]
for e in range(n):
    matrix.append([int(e) for e in input().strip().split()])
for e in range(r):
    r1,c1,r2,c2=[int(e) for e in input().strip().split()]
    if r1>r2 or c1>c2: print("INVALID")
    elif r1>n or r2>n or c1>m or c1>m: print("OUTSIDE")
    else:
        L=[matrix[i][j] for i in range(r1-1,r2) for j in range(c1-1,c2)]
        print(max(L))

