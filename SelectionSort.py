a=list(map(int,input().split()))
b=[0 for i in range(len(a))]
mn,mni=float('inf'),0
curr=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[j]<mn:
            mn=a[j]
            mni=j
    b[i]=mn
    a[mni]=float('inf')
    mn=float('inf')
    mni=0
print(b)
