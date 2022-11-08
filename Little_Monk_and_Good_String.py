s=input()
v="aeiou"
c=0
d=0
for i in s:
    if i in v:
        c+=1
    else:
        if c>d:
            d=c
        c=0
if d==0:
    print(c)
else:
    print(d)