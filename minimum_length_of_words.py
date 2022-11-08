n=input()
l=list(n.split())
min=len(l[0])
for i in l:
    y=str(i)
    x=len(y)
    if x<min:
        min=x
print(min)