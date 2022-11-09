t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=max(l)
    c=0
    d=-1
    for i in range(len(l)-1):
        if l[i]>d and l[i]>l[i+1]:
            c+=1
        if l[i]>d:
            d=l[i]
    if l[-1]>d:
        c+=1
    print("Case #",j+1,": ",c,sep="")