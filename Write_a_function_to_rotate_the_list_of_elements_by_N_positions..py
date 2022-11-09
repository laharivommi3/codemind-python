n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(k):
    l.insert(0,l[-1])
    l.pop(-1)
print(*l)