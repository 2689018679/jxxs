import time

dqtime=time.asctime( time.localtime(time.time()) )

def addrun(time):
    print('当前时间{}'.format(time))
    def addrun1(func):
        def worker(x):
            print('调用者{}'.format(func.__name__).center(20,'-'))
            res=func(x*2)
            flag=True
            # res.sort(reverse=True)
            print(sorted(res,reverse=flag))
        return worker
    return addrun1

@addrun(dqtime)
def run(x):
    return x

for i in range(5):
    run([1,2,3])

l=[]
l.reverse()