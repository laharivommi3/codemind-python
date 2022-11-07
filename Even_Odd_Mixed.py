import math
n=int(input())
e=0
o=0
r=0
d=int(math.log10(n)+1)
while(n>0):
    r=n%10
    if(r%2==0):
        e+=1
    else:
        o+=1
    n=n//10
if(e>=1 and o>=1):
    print("Mixed")
elif(d==e):
    print("Even")
elif(d==o):
    print("Odd")
    