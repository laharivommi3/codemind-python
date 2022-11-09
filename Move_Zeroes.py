n=int(input())
l=list(map(int,input().split()))
j=0
for i in range(len(l)):
    if l[i]!=0:
        l[i],l[j]=l[j],l[i]
        j+=1
print(*l)