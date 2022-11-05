n=int(input())
a=0
b=1
c=0
while(c<=n):
    c=a+b
    a=b
    b=c
if(n-a>b-n):
    print(b)
elif(n-a<b-n):
    print(a)
else:
    print(a,b,end=" ")