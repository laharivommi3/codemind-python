t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    z=[]
    for i in range(n//2):
        z.append(l[-i-1])
        z.append(l[i])
    if n%2!=0:
        z.append(l[n//2])
    print(*z)