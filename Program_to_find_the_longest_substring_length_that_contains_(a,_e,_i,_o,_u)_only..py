s=input()
v="aeiou"
c=0
d=0
x=0
for i in s:
    if i in v:
        c+=1
    else:
        x=1
        if c>d:
            d=c
            c=0
if x==0:
    print(c)
else:
    print(d)