from math import sqrt
t=int(input())
for t in range(1,t+1):
    n=int(input())
    sq=int(sqrt(n))
    if(sq*sq==n):
        print("True")
    else:
        print("False")
    