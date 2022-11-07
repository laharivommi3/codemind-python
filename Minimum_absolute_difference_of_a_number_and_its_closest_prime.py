def isPrime(n):
    c=0
    if(n==1):
        return False
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n=int(input())
if isPrime(n):
    print("0")
else:
    d1=0
    d2=0
    diff1=0
    diff2=0
    for i in range(n+1,10**6):
        if(isPrime(i)):
            d1=i
            break
    diff1=d1-n
    for i in range(n,0,-1):
        if(isPrime(i)):
            d2=i
            break
    diff2=n-d2
print(min(diff1,diff2))