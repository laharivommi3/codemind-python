def reverse(n):
    rev=0
    r=0
    n=abs(n)
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
if(n<0):
    print(-reverse(n),end="")
else:
    print(reverse(n))