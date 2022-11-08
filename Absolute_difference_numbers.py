import math
n,d=map(int,input().split())
len=int(math.log10(n)+1)
d1=int(n%int(10**d))
d2=int(n/int(10**(len-d)))
print(abs(d1-d2))