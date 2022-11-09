n=int(input())
l=list(map(int,input().split()))
s=set(l)
z=[]
for i in s:
    z.append(i)
z.sort()
if n==1:
    print(z[0])
elif n==2:
    print(z[1])
else:
    print(z[-3])