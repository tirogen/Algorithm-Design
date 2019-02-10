def p(l, i):
    if i==0 : return l[0]
    if mem[i]!="o" : return mem[i]
    mem[i]=max(p(l,i-1)+l[i], l[i]);
    return mem[i]

n=int(input().strip())
l=[int(o) for o in input().strip().split()]
mem=["o"]*n
for i in range(n): p(l,i)
while "o" in mem : mem.remove("o")
print(max(mem))
