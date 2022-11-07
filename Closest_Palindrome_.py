def isPalindrome(n):
    r=0
    temp=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==temp):
        return True
    else:
        return False
n=int(input())
d1=0
d2=0
for i in range(n+1,10**6):
    if(isPalindrome(i)):
        d1=i
        break
for i in range(n-1,0,-1):
    if(isPalindrome(i)):
        d2=i
        break
if(n-d2>d1-n):
    print(d1)
elif(n-d2<d1-n):
    print(d2)
else:
    print(d2,d1,end=" ")