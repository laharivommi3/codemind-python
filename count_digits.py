n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(n):
    n=str(abs(l[i]))
    s=0
    s=len(n)
    z.append(s)
print(*z)