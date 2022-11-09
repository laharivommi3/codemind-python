n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    x=str(i)
    if len(x)%2==0:
        c+=1
print(c)