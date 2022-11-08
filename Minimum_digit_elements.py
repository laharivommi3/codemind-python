n=int(input())
l=list(map(int,input().split()))
z=[]
c=0
for i in range(n):
    n=str(abs(l[i]))
    s=0
    s=len(n)
    z.append(s)
mini=z[0]
c=0
for i in z:
    if i<mini:
        mini=i
c=z.count(mini)
print(c)