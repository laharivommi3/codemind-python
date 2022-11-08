def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i;
    return fact
def isStrong(n):
    r=0
    sum=0
    temp=n
    while(temp>0):
        r=temp%10
        sum=sum+fact(r)
        temp=temp//10
    if(sum==n):
        return True
    else:
        return False
n=int(input())
if(isStrong(n)):
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")