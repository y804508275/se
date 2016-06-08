from threading import Thread
import time 
from math import *
precision=3
def calcDis(x1,y1,x2,y2):
    dis=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
    dis=round(sqrt(dis),precision)
    return dis

class race(Thread):
    def __init__(self,threadname, num):
        Thread.__init__(self,name = threadname)
        self.num = num
        self.isrunning = True
        self.maxr = 0

    def start(n,block):
        circle=[]
        while n>0:
            maxr=0
            for i in range(0,10**precision*self.num):
                for j in range(0,10**precision*self.num):
                    x=i/10**precision
                    y=j/10**precision
                    maxr=min(abs(-1-x),abs(1-x),abs(-1-y),abs(1-y))
                    for c in circle:
                        if x==-0.83 and y==-0.83:
                            a=0
                        r=min(r,calcDis(x,y,c[1],c[2])-c[0])
                    for d in block:
                        r=min(r,calcDis(x,y,d[0],d[1]))
                    if r>maxr:
                        maxr=r
                        xm=x
                        ym=y
            circle.append([round(maxr,precision),xm,ym])
            n-=1
        print('thread %s is running, time: %s\n' %(self.getName(), time.ctime()))
        self.maxr = maxr

    def stop(self):
        self.isrunning = False

def test():
    thead1 = race('A',1)
    thead2 = race('B',2)
    thead1.start(5,[])
    thead2.start(5,[])
    time.sleep(5)
    thead1.stop()
    thead2.stop()

if __name__ == '__main__':
    test()