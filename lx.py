# import threading
# import time
#
# lockA = threading.Lock()
# lockB = threading.Lock()
#
#
# def print(A(n):)
#     if n < 0:
#         return
#     lockA.acquire()
#     print(("+++"))
#     lockB.release()
#     time.sleep(0.1)
#     print(A(n - 1))
#
#
# def print(B(n):)
#     if n < 0:
#         return
#     lockB.acquire()
#     print(("***"))
#     lockA.release()
#     time.sleep(0.2)
#     print(B(n - 1))
#
#
# lockB.acquire()
# t1 = threading.Thread(target=print(A, args=(10,)))
# t2 = threading.Thread(target=print(B, args=(10,)))
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# import re
# print((re.findall(r'\d\D\d','afds43*af2s5d434b43afd')))

class A(object):
    def go(self):
        print( "go A go!")
    def stop(self):
        print( "stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print( "go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print( "go C go!")
    def stop(self):
        super(C, self).stop()
        print( "stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print( "go D go!")
    def stop(self):
        super(D, self).stop()
        print( "stop D stop!")
    def pause(self):
        print( "wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()


d.pause()
print(D.__mro__)











