import math
n=int(input())
sq=int(math.sqrt(n))
if sq*(sq+1)==n:
    print("YES")
else:
    print("NO")