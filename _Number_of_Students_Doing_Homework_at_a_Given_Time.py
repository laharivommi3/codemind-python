n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
q=int(input())
c=0
for i in range(n):
    if l1[i]<=q and l2[i]>=q:
        c+=1
print(c)