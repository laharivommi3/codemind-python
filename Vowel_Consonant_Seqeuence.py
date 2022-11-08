s=input()
s1=""
c=0
d=0
v="aeiou"
for i in s:
    if i in v:
        if d!=0:
            s1+="C"
        c+=1
        d=0
    else:
        if c!=0:
            s1+="V"
        c=0
        d+=1
if d!=0:
    s1+="C"
else:
    s1+="V"
print(s1)