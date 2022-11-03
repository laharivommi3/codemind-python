from math import sqrt
n=int(input())
x=int(sqrt(n))
if(x*(x+1)==n):
    print("YES");
else:
    print("NO");
    