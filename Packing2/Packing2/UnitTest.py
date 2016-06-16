from Algorithm import calcCircle
from Algorithm import precision
from random import randint
import time
def genD(n):
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
    print("the number",dlist.index(d)+1,"block location is:",d[0],d[1])
t1=time.time()
print(t1)
clist=calcCircle(n,dlist)
sum=0
for c in clist:
    sum+=c[0]*c[0]
sum=round(sum,precision)
for c in clist:
    print("the number",clist.index(c)+1,"circle location is:",(c[1],c[2]),"radius is:",c[0])
print("the maximum coverage is:",sum)
t2=time.time()
print(t2)
time.sleep(100)
    

