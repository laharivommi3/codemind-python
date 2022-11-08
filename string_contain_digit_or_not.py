n=input()
v="0123456789"
c=0
for i in n:
    if i in v:
        c+=1
if c!=0:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")