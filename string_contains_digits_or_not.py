t=int(input())
v="0123456789"
for i in range(t):
    s=input()
    for i in s:
        if i in v:
            print("Yes")
            break
    else:
        print("No")