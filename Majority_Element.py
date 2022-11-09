n=int(input())
l=list(map(int,input().split(" ")))
c=0
d=0
h=0
s=set(l)
for i in s:
    x=l.count(i)
    if x>n/2:
        c=x
        if c>d:
            d=c
            h=i
print(h)