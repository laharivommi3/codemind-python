def isAutomorphic(n):
    sq=n*n
    while n:
        if(n%10!=sq%10):
            return False
        n//=10
        sq//=10
    return True
n=int(input())
if isAutomorphic(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")