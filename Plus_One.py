n=int(input())
l=list(map(int,input().split()))
res=int("".join(map(str,l)))
res=res+1
s=list(map(int,str(res)))
print(*s)