s=input()
s1=""
s1+=s[0]
s1+=s[1]
s1=int(s1)
x=s1
if s1>12:
    s1=abs(12-s1)
if s1==0:
    s1=12
so=""
if x>=12:
    if s1<10:
        so+="0"
    so+=str(s1)
    so+=":"
    so+=s[3]
    so+=s[4]
    so+=" "
    so+="PM"
else:
    if s1<10:
        so+="0"
    so+=str(s1)
    so+=":"
    so+=s[3]
    so+=s[4]
    so+=" "
    so+="AM"
print(so)