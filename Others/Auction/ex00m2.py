Ntypes, Musers, Alines = [int(e) for e in input().strip().split()]
Nitems = [0]+[int(e) for e in input().strip().split()]

bagKetByType = [{}]+[{} for i in range(Ntypes)]

for _ in range(Alines):
    inp = input().strip().split()
    if inp[0] == "B":
        bagKetByType[int(inp[2])][int(inp[1])] = int(inp[3])
    else:
        if int(inp[1]) in bagKetByType[int(inp[2])]:
            bagKetByType[int(inp[2])].pop(int(inp[1]))
        
#example value of bagKetByType = [{}, {1: 10, 2: 100}, {1: 99, 2: 100}]
#                                      ^user           |<---items--->|

bagKetByUsers = [[]]+[[] for i in range(Musers)]

for i in range(1,Ntypes+1):
    for item in sorted(bagKetByType[i].items(), key=lambda x:(-x[1],-x[0]))[:Nitems[i]]:
        #example bid win [(2, 100), (1, 99)] of item i
        bagKetByUsers[item[0]].append(str(i))


#example value of bagKetByUsers = [[], [], ['1', '2'], []]
for i in range(1,Musers+1):
    if len(bagKetByUsers[i]) == 0:
        print("NONE")
    else:
        print(" ".join(bagKetByUsers[i]))
