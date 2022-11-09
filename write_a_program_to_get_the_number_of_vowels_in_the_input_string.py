n=input()
x=list(n)
s=0
v="aeiouAEIOU"
for i in x:
    if i in v:
        s+=1
print(s)