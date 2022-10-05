def Rec(dist):
    if dist<0:
        return 0
    if dist==0:
        return 1
    return(Rec(dist-1)+Rec(dist-2)+Rec(dist-3))
dist=int(input())
print(Rec(dist))