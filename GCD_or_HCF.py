x,y=map(int,input().split())
if x>y:
    min=y
else:
    min=x
for i in range(1,min+1):
    if(x%i==0 and y%i==0):
        hcf=i
print(hcf)