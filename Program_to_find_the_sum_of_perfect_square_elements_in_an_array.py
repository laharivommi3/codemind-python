def perfect(n):
    sq=int(n**0.5)
    if sq*sq==n:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if perfect(i):
        c+=i
print(c)