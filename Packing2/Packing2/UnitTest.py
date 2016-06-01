from Algorithm import calcCircle
from Algorithm import precision
from random import randint
def genD(d):
    dlist=[]
    for i in range(d):
        x=randint(-10**precision,10**precision)
        y=randint(-10**precision,10**precision)
        dlist.append([x/10**precision,y/10**precision])
    return dlist
n=int(input("please input circle number:"))
d=int(input("please input block number:"))
dlist=genD(d)
for d in dlist:
    print(d[0],d[1])
clist=calcCircle(n,dlist)
sum=0
for c in clist:
    sum+=c[0]*c[0]
sum=round(sum,precision)
print("the maximum coverage is:",sum)

    

