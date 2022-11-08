s=input()
c=1
d=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        if c>d:
            d=c
        c=1
if c==1:
    print(d)
else:
    print(c)