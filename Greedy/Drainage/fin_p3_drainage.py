from sys import stdin as kb

n,l=map(int,kb.readline().split())
x=sorted(list(map(int,kb.readline().split())))
edge=0
count=0
for o in x:
    if o>edge:
        count+=1
        edge=o+l-1
print(count)
