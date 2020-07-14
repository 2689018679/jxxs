# import threading,time
# class Boss(threading.Thread):
#     def run(self):
#         print("BOSS：今晚大家都要加班到22:00。")
#         print(event.isSet())
#         event.set()
#         time.sleep(5)
#         print("BOSS：<22:00>可以下班了。")
#         print(event.isSet())
#         event.set()
# class Worker(threading.Thread):
#     def run(self):
#         event.wait()
#         print("Worker：哎……命苦啊！")
#         time.sleep(1)
#         event.clear()
#         event.wait()
#         print("Worker：OhYeah!")
# from queue import Queue
# if __name__=="__main__":
#     event=threading.Event()
#     threads=[]
#     for i in range(5):
#         threads.append(Worker())
#     threads.append(Boss())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()



#
# import queue  #队列，解决多线程问题  （注意：python2.7 Queue的首字母是大写的）
#
#
# # q=queue.Queue(3) #1、设置3就是满了，默认（FIFO 先进先出 ） #先进后出（手枪弹夹，后压进去的，先出来）
# q=queue.Queue(3)
# q.put(12)
# q.put("hello")
# q.put({"name":"yuan"})
#
# q.put(34,1)
# # q.put(34,False) #2、blook=True,如果改成Flase,提示你满了，会报错，但不会卡在这里
#
#
# while 1:
#     data=q.get()  #1、会卡着，等值进来
#     # data=q.get(block=False)  #3、队列为空
#     print(data)
#     print("-----------")



#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige


#
# #管道
# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([12, {"name":"yuan"}, 'hello']) #发送消息
#     response=conn.recv()  #接收消息
#     print("response",response)
#     conn.close()
#     print("q_ID2:",id(conn))
#
# if __name__ == '__main__':
#
#     parent_conn=Pipe()
#     child_conn = Pipe()
#     print("q_ID1:",id(child_conn))
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#
#     print(parent_conn.recv())    #接收消息 prints "[42, None, 'hello']"
#     parent_conn.send("儿子你好!")  #发送消息
#     p.join()


#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: nulige
#
# from multiprocessing import Process, Manager
#
# def f(d, l,n):
#     d[n] = '1'  #{0:"1"}
#     d['2'] = 2  #{0:"1","2":2}
#     l.append(n) #[0.1.2.3.4.0]
#     # print(l)
#     print("son process:",id(d),id(l))
#
# if __name__ == '__main__':
#
#     with Manager() as manager:  #用with相当于打开文件就不要关闭了
#
#         d = manager.dict()  #{}  #主进程
#
#         l = manager.list(range(5)) #[0,1,2,3,4]
#
#         print("main process:",id(d),id(l))
#
#         p_list = []
#
#         for i in range(10): #10个子进程
#             p = Process(target=f, args=(d,l,i))  #主进程传过去
#             p.start()
#             p_list.append(p)
#
#         for res in p_list:
#             res.join()
#
#         print(d)
#         print(l)




from  multiprocessing import Process,Pool
import time,os

def Foo(i):
    time.sleep(1)
    print(i)
    print("son:",os.getpid())
    return "HELLO %s "%i

def Bar(arg):  #回调函数
    print('hui'.center(10,'*'))
    print(arg)
    # print("hello")
    # print("Bar:",os.getpid())

if __name__ == '__main__':

    pool = Pool(5)  #进程池的数量
    print("main pid", os.getpid())
    for i in range(10):  #进程数
        #pool.apply(func=Foo, args=(i,))
        # pool.apply_async(func=Foo, args=(i,))

        #回调函数: 就是某个动作或者函数执行成功后再去执行的函数
        pool.apply_async(func=Foo, args=(i,),callback=Bar)

    pool.close()
    pool.join()
    print('end')














