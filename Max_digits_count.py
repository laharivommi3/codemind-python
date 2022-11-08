n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(n):
    n=str(abs(l[i]))
    s=0
    s=len(n)
    z.append(s)
max=z[0]
for i in z:
    if i>max:
        max=i
c=0
c=z.count(max)
print(c)