s=input()
v="aeiou"
d="0123456789"
v1=0
c1=0
d1=0
s1=0
for i in s:
    if i in v:
        v1+=1
    elif i.isalpha() and i not in v:
        c1+=1
    elif i in d:
        d1+=1
    else:
        s1+=1
print("Vowels:",v1)
print("Consonants:",c1)
print("Digits:",d1)
print("White spaces:",s1)
        