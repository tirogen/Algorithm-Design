mem = [[-1 for j in range(500)] for i in range(500)]

def lcs(one, two, p1, p2):
    if p1==len(one) or p2==len(two) : return 0
    if mem[p1][p2]!=-1 : return mem[p1][p2]
    if one[p1]==two[p2] :
        mem[p1][p2] = 1+lcs(one, two, p1+1, p2+1)
    else :
        mem[p1][p2] = max(lcs(one,two,p1+1,p2), lcs(one,two,p1,p2+1))
    return mem[p1][p2]

one = input().strip()
two = input().strip()
print(lcs(one ,two ,0 ,0))
