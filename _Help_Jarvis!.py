t=int(input())
for i in range(t):
    n=int(input())
    n=str(n)
    n=sorted(n)
    for i in range(1,len(n)):
        if int(n[i])-int(n[i-1])!=1:
            print("NO")
            break
    else:
        print("YES")