n=input()
k=input()
x=list(n)
r=0
for i in range(len(x)):
    if x[i]==k:
        print("True")
        print(i)
        break
    r+=1
else:
    print("False")