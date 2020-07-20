import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay) # results in 10s of execution time with no_of_tasks set to 10
    # time.sleep(delay) #results in 55.01 seconds of execution time with no_of_tasks set to 10
    print(what)


async def main():
    no_of_tasks = 10
    task_queue=[]
    # task1 = asyncio.create_task(
    #     say_after(1, 'hello'))

    # task2 = asyncio.create_task(
    #     say_after(2, 'world'))
    for index in range(0, no_of_tasks):
        task_queue.append(asyncio.create_task(say_after(index+1,f"hello {index+1}")))
    # print(f"started at {time.strftime('%X')}")
    s = time.perf_counter()

    # Wait until both tasks are completed (should take
    # around 2 seconds.)

    # await task1
    # await task2

    for index in range(0, no_of_tasks):
        await task_queue[index]

    # print(f"finished at {time.strftime('%X')} and difference is {}")
    
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
asyncio.run(main())
