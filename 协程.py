# import asyncio
#
#
# async def work(x):  # 通过async关键字定义一个协程
#     for _ in range(3):
#         print('Work {} is running ..'.format(x))
#     await asyncio.sleep(1)
#
# coroutine_1 = work(1)  # 协程是一个对象，不能直接运行
#
# # 方式一：
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# result = loop.run_until_complete(coroutine_1)  # 将协程对象加入到事件循环中，并执行
# print(result)  # 协程对象并没有返回结果，打印None
# 方式二：
# asyncio.run(coroutine_1)  #创建一个新的事件循环，并以coroutine_1为程序的主入口，执行完毕后关闭事件循环


# import asyncio
#
#
# async def work(x):
#     for _ in range(3):
#         print('Work {} is running ..'.format(x))
#     return "Work {} is finished".format(x)
#
#
# def call_back(future):
#     print("Callback: {}".format(future.result()))
#
#
# coroutine = work(1)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(call_back)
# loop.run_until_complete(task)  # 返回任务的结果


# import asyncio, time
#
#
# async def work(x):
#     for _ in range(3):
#         print("Work {} is running ..".format(x))
#         await asyncio.sleep(1)  # 当执行某个协程时，在任务阻塞的时候用await挂起
#     return "Work {} is finished!".format(x)
#
#
# async def main_work():
#     coroutine_1 = work(1)
#     coroutine_2 = work(2)
#     coroutine_3 = work(3)
#
#     tasks = [
#         asyncio.ensure_future(coroutine_1),
#         asyncio.ensure_future(coroutine_2),
#         asyncio.ensure_future(coroutine_3),
#     ]
#
#     dones, pendings = await asyncio.wait(tasks)
#
#     for task in dones:
#         print("The task's result is : {}".format(task.result()))
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main_work())


# 使用as_completed方法

import asyncio


async def work(x):
    for _ in range(3):
        print("Work {} is running ..".format(x))
        await asyncio.sleep(1)  # 当执行某个协程时，在任务阻塞的时候用await挂起
    return "Work {} is finished!".format(x)


async def main_work():
    coroutine_1 = work(1)
    coroutine_2 = work(2)
    coroutine_3 = work(3)

    tasks = [
        asyncio.ensure_future(coroutine_2),
        asyncio.ensure_future(coroutine_1),
        asyncio.ensure_future(coroutine_3),
    ]

    for task in asyncio.as_completed(tasks):  # 返回一个可迭代对象，每次返回最先完成的任务的结果
        result = await task
        print(f"The task's result is : {result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_work())




























