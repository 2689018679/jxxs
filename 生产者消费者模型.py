#生产者消费者模型（生产者先执行，再吃包子。）

import time,random
import queue,threading

q = queue.Queue()

def Producer(name):
  count = 0
  while count <10:
    print("制作中".center(10,'-'))
    time.sleep(random.randrange(3)) #产生一个随机数（1-2秒之间）
    q.put(count)
    print('%s 制作 %s 包子..' %(name, count))
    count +=1
    print("完成".center(10,'*'))

def Consumer(name):
  count = 0
  while count <10:
    time.sleep(random.randrange(4))  #产生一个随机数（1-3秒之间）
    if not q.empty():
        data = q.get()
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
    else:
        print("-----没有了----")
        count +=1

p1 = threading.Thread(target=Producer, args=('A君',))
c1 = threading.Thread(target=Consumer, args=('B君',))

p1.start()
c1.start()