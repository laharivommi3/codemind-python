n=input()
n=list(n.split())
for i in range(len(n)-1,-1,-1):
    print(n[i][::-1],end=" ")