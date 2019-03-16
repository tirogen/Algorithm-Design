Ntypes, Musers, Alines = [int(e) for e in input().strip().split()]
Nitems = [0]+[int(e) for e in input().strip().split()]

#bagKetByType = [{}]+[{} for i in range(Ntypes)]
bagKetByType = dict()

for _ in range(Alines):
    inp = input().strip().split()
    if inp[0] == "B":
        if int(inp[2]) not in bagKetByType:
            bagKetByType[int(inp[2])] = {int(inp[1]):int(inp[3])}
        else:
            bagKetByType[int(inp[2])][int(inp[1])] = int(inp[3])
    else:
        if int(inp[2]) in bagKetByType:
            if int(inp[1]) in bagKetByType[int(inp[2])]:
                bagKetByType[int(inp[2])].pop(int(inp[1]))
        
#example value of bagKetByType = {1: {1: 10, 2: 100}, 2: {1: 99, 2: 98}}
#                                     ^label          ^item

bagKetByUsers = [[] for i in range(Musers)]

for key in bagKetByType.keys():
    for item in sorted(bagKetByType[key].items(), reverse = True)[:Nitems[key]]:
        #example bid win [(2, 100), (1, 99)] of item i
        bagKetByUsers[item[0]-1].append(str(key))


#example value of bagKetByUsers = [[], [], ['1', '2'], []]
for i in range(Musers):
    if len(bagKetByUsers[i]) == 0:
        print("NONE")
    else:
        print(" ".join(bagKetByUsers[i]))
