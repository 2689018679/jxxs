# 创建两个线程，其中一个输出1-52，另外一个输出A-Z。输出格式要求：12A 34B 56C 78D
import threading

t=threading.Lock()
t1=threading.Lock()

class Num(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,53,2):
            t.acquire()
            print(i,end='')
            print(i+1,end='')
            t1.release()

class Str(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(ord('A'),ord('Z')+1):
            t1.acquire()
            print(chr(i))
            t.release()


if __name__=='__main__':
    n=Num()
    s=Str()
    t1.acquire()
    n.start()
    s.start()
    n.join()
    s.join()












# 生成器
# print('生成器:',end='')
# print((i for i in range(10)))
# 推导式、
# print('推导式:',end='')
# print([i for i in range(10)])
# 匿名函数
# print('匿名函数:',end='')
# print([i for i in map(lambda x:x**2,range(1,6))])
# 进程、
from multiprocessing import Process

# 线程、
# 装饰器

# def addname(name):
#     def worker(fun):
#         def worker_add():
#             print('正在运行{0}()内容{1}'.format(fun.__name__,name))
#             return fun()
#         return worker_add
#     return worker
#
# @addname(123)
# def hello():
#     print('hello')
# hello()