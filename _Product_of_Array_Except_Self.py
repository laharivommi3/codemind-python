n=int(input())
l=list(map(int,input().split()))
z=[]
s=1
for i in range(n):
    s*=l[i]
for i in range(n):
    z.append(s//l[i])
print(*z)