import math
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
d=int(math.log10(n)+1)
r=0
count=0
if isPrime(n):
    while n>0:
        r=n%10
        n=n//10
        if isPrime(r):
            count+=1
if(count==d):
    print("Mega Prime")
else:
    print("Not Mega Prime")
            