n=int(input())
arr=list(map(int,input().strip().split()))
x=0
for i in range(0,len(arr)):
    x=x+arr[i]
print(x)