import math
n=int(input())
d=int(math.log10(n)+1)
sum=0
r=0
temp=n
while n>0:
    r=n%10
    sum=sum+r**d
    n=n//10
    d-=1
if(sum==temp):
    print("True")
else:
    print("False")