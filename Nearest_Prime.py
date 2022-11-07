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
t=int(input())
for t in range(1,t+1):
    n=int(input())
    d1=0
    d2=0
    for i in range(n+1,10**6):
        if(isPrime(i)):
            d1=i
            break
    for i in range(n,0,-1):
        if(isPrime(i)):
            d2=i
            break
    if(n-d2>d1-n):
        print(d1)
    elif(n-d2<d1-n):
        print(d2)
    else:
        print(min(d1,d2))
            