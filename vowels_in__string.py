n=input()
x=list(n)
z=list()
v="aeiouAEIOU";
for i in x:
    if i in v:
        z.append(i)
y=[]
for i in range(len(z)):
    c=0
    for j in range(i+1):
        if z[i]==z[j]:
            c+=1
    if c==1:
        y.append(z[i])
if y==[]:
    print(-1)
else:
    print(*y)
    