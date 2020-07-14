# 进程
# from multiprocessing import Process,Manager,Queue
# import time,random
#
# def scz(g):
#     while 1:
#         time.sleep(random.randrange(0,2))
#         if not g.full():
#             g.put(0)
#         print('生产{}'.format(g.qsize()))
#
# def xfz(g):
#     while 1:
#         time.sleep(random.randrange(3,5))
#         if not g.empty():
#             g.get()
#         print('消费'+str(g.qsize()))
#
#
# if __name__=='__main__':
#     # with Manager() as m:
#     #     guo=m.list()
#     #     p=Process(target=scz,args=(guo,))
#     #     p.start()
#     #     p1=Process(target=xfz,args=(guo,))
#     #     p1.start()
#     #     p.join()
#     #     p.join()
#     #     print(guo)
#     guo=Queue(10)
#     p = Process(target=scz, args=(guo,))
#     p.start()
#     p_list=[]
#     for i in range(5):
#         p1=Process(target=xfz,args=(guo,))
#         p1.start()
#         p_list.append(p1)
#     for i in p_list:
#         i.join()
#     p.join()



# 线程
# import threading,time
#
# class scz(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#     def run(self):
#         while 1:
#             time.sleep(2)
#             print('生产')
#             e.set()
#
#
# class xfz(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         while 1:
#             e.wait()
#             print('消费')
#             e.clear()
#
# if __name__=='__main__':
#     e=threading.Event()
#     cs=scz(5)
#     cs.start()
#     gk_list=[]
#     for i in range(5):
#         gk=xfz()
#         gk.start()
#         gk_list.append(gk)
#     cs.join()
#     for i in gk_list:
#         i.join()

# 装饰器
# def addname(name):
#     def work(fun):
#         def addword():
#             print('hello'+name)
#             return fun
#         return addword
#     return work
#
# @addname('123')
# def hello():
#     print('hello')

# hello()

# 生成器
# def run(x):
#     while True:
#         print(x)
#         s=yield x
#         print(s)
# g=run(1)
# next(g)
# g.send('2ci')

# 推导式
# print([x for x in range(10)])

# 匿名函数
# def pf(x):
#     return x*x
# a=range(10)
# print([i for i in map(pf,a)])
# print([i for i in map(lambda x:x*x-1,range(10))])

# 协程

import asyncio

async def run():
    print(123)
    return 'ok'

def call(data):
    print(data._result)

if __name__ == '__main__':
    l = asyncio.get_event_loop()  # 创建事件循环
    res = l.run_until_complete(run())  # 将协程对象添加到事件循环
    t = l.create_task(run())  # 创建task对象
    t.add_done_callback(call)  # 为task对象绑定回调函数
    l.run_until_complete(t)  # 将task对象添加到事件循环