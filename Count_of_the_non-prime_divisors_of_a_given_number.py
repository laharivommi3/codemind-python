def isPrime(n: int) ->bool:
    count=0
    if(n<=1):
        return False
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        return True
    else:
        return False
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if isPrime(i):
            continue
        else:
            c+=1
print(c)