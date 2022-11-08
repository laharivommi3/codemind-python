n=int(input())
l=list(map(int,input().split()))
z=[]
y=[]
mx=0
for i in range(n):
    n=str(abs(l[i]))
    s=0
    s=len(n)
    z.append(l[i])
    if s>mx:
        mx=s
for i in z:
    n=str(abs(i))
    s=0
    s=len(n)
    if s==mx:
        y.append(i)
v=[]
for i in y:
    c=0
    for j in y:
        if i==j:
            c+=1
    if c==1:
        v.append(i)
print(*v)