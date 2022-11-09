t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=sum(l)
    y=(n*(n+1))//2
    print(y-x)