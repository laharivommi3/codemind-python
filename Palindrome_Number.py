t=int(input())
for t in range(1,t+1):
    n=int(input())
    temp=n
    r=0
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(temp==rev):
        print("True")
    else:
        print("False")