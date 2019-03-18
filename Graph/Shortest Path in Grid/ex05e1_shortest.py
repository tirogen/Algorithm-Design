r,c = map(int, input().split())
M = []
C = []
for _ in range(r):
    M.append([0 if s=="#" else 1 for s in input().strip()])
    C.append([False]*c)

H = []
H.append((0,0,0))
C[0][0] = True

while len(H)>0:
    d,i,j = H.pop(0)
    if i == c-1 and j == r-1:
        print(d)
        break
    for x,y in {(0,1), (1,0), (-1, 0), (0, -1)}:
        if i+x < c and i+x >= 0 and j+y < r and j+y >= 0\
           and not C[j+y][i+x] and M[j+y][i+x]==1:
            C[j+y][i+x] = True
            H.append((d+1, i+x, j+y))
else:
    print(-1)
