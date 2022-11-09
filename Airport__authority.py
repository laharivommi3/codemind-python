n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
k=int(input())
s=0
for i in l:
    if i>k:
        s+=2
    else:
        s+=1
print(s)