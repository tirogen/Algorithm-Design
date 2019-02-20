import bisect as bs

n=int(input())
x=[]
for e in range(n):
    x.append(int(input()))
L=[0,1,3]
MAX = max(x)
num = 3
while L[-1]<MAX:
    i = bs.bisect_left(L,num)
    L.append(L[-1]+i)
    num += 1
for o in x:
    print(bs.bisect_left(L, o))
