s=input()
s1=""
s1+=s[0]
s1+=s[1]
s1=int(s1)
if s1==12:
    if s[6]=="A":
        s1=00
elif s1<12:
    if s[6]=="P":
        s1=12+s1
so=""
if s1<10:
    so+="0"
so+=str(s1)
so+=":"
so+=s[3]
so+=s[4]
print(so)