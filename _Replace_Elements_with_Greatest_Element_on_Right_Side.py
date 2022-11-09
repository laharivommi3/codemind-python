n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(n-1):
    mx=0
    for j in range(i+1,n):
        if l[j]>mx:
            mx=l[j]
    z.append(mx)
z.append(-1)
print(*z)