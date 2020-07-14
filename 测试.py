import threading,time

# l=threading.Lock()
# g=[]
# def scz():
#     while True:
#         g.append(0)
#
# def xfz():
#     while 1:
#         del(g[0])
#
# if __name__=='__main__':
#     tlist=[]
#     for i in range(5):
#         t=threading.Thread(target=run,args=(i,l,))
#         t.start()
#         tlist.append(t)
#     for t in tlist:
#         t.join()


# import asyncio
# a=10
# async def f(x):
#     global a
#     a-=1
#     print(a)
#
# async def g(x):
#     global a
#     a-=1
#     print(a)
#
# asyncio.run(f(a))
# asyncio.run(g(a))

a=0

def changex(fun):
    def work(b):
        if b>1:
            b=1
        return fun(b)
    return work

@changex
def hello(b):
    print(b)

hello(314)








