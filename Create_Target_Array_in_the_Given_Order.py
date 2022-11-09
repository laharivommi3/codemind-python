n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
t=[]
for i in range(n):
    t.insert(l2[i],l1[i])
print(*t)