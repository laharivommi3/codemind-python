n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(0,n,2):
    x=l[i]
    y=l[i+1]
    for i in range(x):
        z.append(y)
print(*z)