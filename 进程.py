# from multiprocessing import Process
# import time
# import os
#
# #继承Process类
# class Process_Class(Process):
#     # 模块中，Process类本身有__init__方法，现在这个子类重写Process方法
#     # 导致无法完全初始化一个Process类，进而就不能从这个类继承的一些方法和属性
#     # 解决方法，将继承类本身传递给Process.__init__，完成初始化操作
#     def __init__(self,interval):
#         Process.__init__(self)
#         self.interval = interval
#
#     #重写了Process类的run()方法
#     def run(self):
#         print("子进程(%s) 开始执行，父进程为（%s）"%(os.getpid(),os.getppid()))
#         t_start = time.time()
#         time.sleep(self.interval)
#         t_stop = time.time()
#         print("(%s)执行结束，耗时%0.2f秒"%(os.getpid(),t_stop-t_start))
#
# if __name__=="__main__":
#     t_start = time.time()
#     print("当前程序进程(%s)"%os.getpid())
#     p1 = Process_Class(2)
#     p1.start()
#     p1.join()
#     t_stop = time.time()
#     print("(%s)执行结束，耗时%0.2f"%(os.getpid(),t_stop-t_start))


# from multiprocessing import Pool
# import os
# import time
# import random
#
# def worker(msg):
#     t_start = time.time()
#     print("%s开始执行，进程号为%d" % (msg,os.getpid()))
#     time.sleep(random.random()*2)
#     t_stop = time.time()
#     print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))
#
# if __name__ == '__main__':
#     po =  Pool(3) # 定义进程池，最大进程数为3
#     for i in range(0,10):
#         po.apply(worker,(i,))
#
#     print("start".center(11,"-"))
#     po.close()
#     po.join()
#     print("end".center(11, "-"))

#
#
from multiprocessing import Process, Queue
import os
import time
import random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 等待pw结束:
    pw.join()
    # 启动子进程pr，读取:
    pr.start()
    pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('')
    print('所有数据都写入并且读完')