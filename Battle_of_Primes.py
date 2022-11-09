def isPrime(n):
    c=0
    for i in range(2,int(n/2)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n1=int(input())
n2=int(input())
sum=n1+n2
count=0
for i in range(sum+1,10**6):
    count+=1
    if isPrime(i):
        break;
print(count)