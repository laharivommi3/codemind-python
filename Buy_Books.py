n=int(input())
m=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(m)>=sum(b):
    print(0)
else:
    s1=sum(m)
    s2=sum(b)
    print(s2-s1)