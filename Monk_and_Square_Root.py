import math
t=int(input())
for t in range(1,t+1):
    m,n=map(int,input().split())
    chk=0
    for i in range(int(math.floor(math.sqrt(m))),n//2+1):
        if(i*i)%n==m:
            print(i)
            chk=1
            break
    if chk==0:
            print("-1")