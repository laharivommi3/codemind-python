def isPrime(n: int) -> bool:
    c=0
    if(n<=1):
        return False
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if isPrime(i):
        print(i);