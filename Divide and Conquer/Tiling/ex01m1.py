def tiling(x,y,i,j,d):
    global L
    if d == 2:
        if x == i:
            if y == j: L.append((0,i,j))
            else: L.append((2,i,j))
        else:
            if y == j: L.append((1,i,j))
            else: L.append((3,i,j))
        return
    if y < j+d//2:
        if x < i+d//2:#Q2
            L.append((0,i+d//2-1,j+d//2-1))
            tiling(x,           y,              i,          j,          d//2) #above-left
            tiling(i+d//2,      j+d//2-1,       i+d//2,     j,          d//2) #above-right
            tiling(i+d//2-1,    j+d//2,         i,          j+d//2,     d//2) #bottom-left
            tiling(i+d//2,      j+d//2,         i+d//2,     j+d//2,     d//2) #bottom-right
        else:#Q1
            L.append((1,i+d//2-1,j+d//2-1))
            tiling(i+d//2-1,    j+d//2-1,       i,          j,          d//2) #above-left
            tiling(x,           y,              i+d//2,     j,          d//2) #above-right
            tiling(i+d//2-1,    j+d//2,         i,          j+d//2,     d//2) #bottom-left
            tiling(i+d//2,      j+d//2,         i+d//2,     j+d//2,     d//2) #bottom-right
    else:
        if x < i+d//2:#Q3
            L.append((2,i+d//2-1,j+d//2-1))
            tiling(i+d//2-1,    j+d//2-1,       i,          j,          d//2) #above-left
            tiling(i+d//2,      j+d//2-1,       i+d//2,     j,          d//2) #above-right
            tiling(x,           y,              i,          j+d//2,     d//2) #bottom-left
            tiling(i+d//2,      j+d//2,         i+d//2,     j+d//2,     d//2) #bottom-right
        else:#Q4
            L.append((3,i+d//2-1,j+d//2-1))
            tiling(i+d//2-1,    j+d//2-1,       i,          j,          d//2) #above-left
            tiling(i+d//2,      j+d//2-1,       i+d//2,     j,          d//2) #above-right
            tiling(i+d//2-1,    j+d//2,         i,          j+d//2,     d//2) #bottom-left
            tiling(x,           y,              i+d//2,     j+d//2,     d//2) #bottom-right
    return

L = []
n,x,y = [int(e) for e in input().strip().split()]
tiling(x,y,0,0,n)
print(len(L))
for e in L:
    print(e[0],e[1],e[2])
