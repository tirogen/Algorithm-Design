def G(n):
    g="gaa"
    zum=3
    i=1
    while zum<n:
        if n<=zum+i+3:
            if n==zum+1: return "g"
            else: return "a"
        if n<=2*zum+i+3:
            if n==zum+i+4: return "g"
            else: return "a"
        g=g+"g"+"a"*(i+2)+g
        zum=2*zum+1+(i+2)
        i+=1
    return g[n-1]

n=int(input().strip())

print(G(n))
