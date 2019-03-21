from sys import stdin as kb
import copy
p=int(kb.readline())

for _ in range(p):
  n=int(kb.readline())
  g=[[0]*n for _ in range(n)]
  for i in range(n):
    tmp=[float(e) for e in kb.readline().split()]
    for j in range(n):
      g[i][j]=tmp[j]

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if g[i][k]*g[k][j]>g[i][j]:
          g[i][j]=g[i][k]*g[k][j]
          if g[i][j]>1 and i==j:
            print("YES")
            break
      else:
        continue
      break
    else:
      continue
    break
  else:
    print("NO")
