n,k=map(int,input().split( ))
l=list(map(int,input().split()))
c=0
for i in range(n):
    n=str(abs(l[i]))
    s=0
    s=len(n)
    if s==k:
        c+=1
print(c)