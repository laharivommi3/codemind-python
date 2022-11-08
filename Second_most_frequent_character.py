s=input()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s=dict(sorted(d.items(),key=lambda item:item[1]))
l=[]
for i in d:
    l.append(d[i])
l=set(l)
l=sorted(l)
if len(l)==1:
    print("-1")
else:
    h=l[-2]
    print(list(d.keys())[list(d.values()).index(h)])
