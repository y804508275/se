import time
class Employee:
   def __init__(self, a, b,c):
      self.a = a
      self.b = b
      self.c = c

circle=Employee(1.01,1.02,1.03)
c=[1.01,1.03,1.04]
a=time.ctime()
print(a)
b=0
for i in range(100000000):
    b+=circle.a+circle.b+circle.c
a=time.ctime()
print(a)
b=0
for i in range(100000000):
    b+=c[0]+c[1]+c[2]
a=time.ctime()
print(a)
a=0