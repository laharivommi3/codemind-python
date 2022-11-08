s=input()
v="1234567890"
count=0
for i in s:
    if i in v:
        count+=int(i)
print(count)