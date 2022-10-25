def isPalindrome(n: int) -> bool:
    rev=0
    temp=n
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(temp==rev):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if isPalindrome(i):
        print(i,end=" ")