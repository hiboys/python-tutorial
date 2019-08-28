# 好奇 task 是一个什么结构? 起到什么作用
# asyncio 的 event loop api 体现了集中式的特点
# 怎么用 asycio 来读取一个文件

import asyncio


async def another_task_func():
    print("in another task")
    return "another task result"


# 简单协程
async def task_func():
    print("in task")
    r = await another_task_func()
    print(r)
    return "task func result"

if __name__ == "__main__":
    # 创建事件循环
    loop = asyncio.get_event_loop()

    # 创建任务
    # 创建任务的同时，其实已经将任务加入到 event loop 中
    task = loop.create_task(task_func())

    # 运行直到完成
    print("start event loop")
    #loop.run_until_complete(task)

    # 永远运行的世界循环
    loop.run_forever()
    print("end event loop")

