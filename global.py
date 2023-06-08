#global scope, local scope

a = 5 #global
import time
#def f(): #global
    #print(a) #global

#def g():
    #a = 3 #local
    #print(a) #local
#g()
#print(a)

#def h():
    #a += 3 local
    #print(a) local
#h()

def j():
    global a
    a += 3 #global
    print(a)

j()

a = 5
def f():
    a = 4 #local ของf
    def g():
        a = 2
#f()

def gcd(x, y):
    for d in range(1000, 0, -1):
        if x % d == 0 and y % d == 0:
            break
    return d

t1 = time.time()
print(gcd(88, 11))
t2 = time.time()
print(gcd(88, 11))