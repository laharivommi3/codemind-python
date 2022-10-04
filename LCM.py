x,y=map(int,input().split())
lcm=0
if x>y:
    max=x
else:
    max=y
while True:
    if(max%x==0 and max%y==0):
        print(max)
        break
    max+=1

        