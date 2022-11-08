t=int(input())
for i in range(t):
    s=input()
    v="0123456789"
    c=0
    for i in s:
        if i in v:
            c+=1
    if len(s)==c:
        print(True)
    else:
        print(False)