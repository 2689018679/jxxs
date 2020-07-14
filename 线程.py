import threading

i=[]
l=threading.Lock()
class Sheng(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i
    def run(self):
        if l.acquire():
            for j in range(5):
                 i.append(j)
                 print('生产')
                 print(i)
            l.release()


class Eat(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i
    def run(self):
        if l.acquire():
            for j in range(5):
                 i.pop(0)
                 print('吃')
                 print(i)
            l.release()


if __name__=="__main__":
    s=Sheng(i)
    e=Eat(i)
    s.start()
    e.start()


#
#
#
#
#
#
#
#
# import threading
#
# # global var
# count = 0
#
# # Define a function for the thread
# def print_time(threadName):
#     global count
#
#     c=0
#     while(c<100):
#         c+=1
#         count+=1
#         print("{0}: set count to {1}".format( threadName, count) )
#
# # Create and run threads as follows
# try:
#     threading.Thread( target=print_time, args=("Thread-1", ) ).start()
#     threading.Thread( target=print_time, args=("Thread-2", ) ).start()
#     threading.Thread( target=print_time, args=("Thread-3", ) ).start()
# except Exception as e:
#     print("Error: unable to start thread")
