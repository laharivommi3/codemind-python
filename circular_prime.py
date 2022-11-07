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
def reverse(n):
    r=0
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
if(isPrime(reverse(n))):
    print("circular prime")
elif(isPrime(n) and (not(isPrime(reverse(n))))):
    print("prime but not a circular prime")
else:
    print("not prime")