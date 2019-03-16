import sys
kb = sys.stdin

def bs(l,r,s):
    if l>r: return -1
    if l==r: return L[l] if s>=L[l] else -1
    mid=(l+r)//2
    if L[mid]<=s and L[mid+1]>s:
        return L[mid]
    elif L[mid]<s:
        return bs(mid+1,r,s)
    elif L[mid]==s and L[mid+1]==s:
        return bs(mid+1,r,s)
    elif L[mid]==s:
        return L[mid]
    else:
        return bs(l,mid-1,s)

n,m=[int(e) for e in kb.readline().strip().split()]
L=[int(e) for e in kb.readline().split()]
M=[int(e) for e in kb.readline().split()]

for e in M:
    print(bs(0,n-1,e))
