from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from time import perf_counter
def cpu_heavy():
    count = 0
    for i in range(10**6):
        count += i

if __name__=="__main__":
    no_of_tasks=25
    print(f"Running {no_of_tasks} task serially...")
    start_time=perf_counter()
    for _ in range(0,no_of_tasks):
        cpu_heavy()
    print(f"Runtime for serial tasks is {perf_counter()-start_time}")
    print(f"Running {no_of_tasks} tasks using multiprocessing...")
    start_time=perf_counter()
    with ProcessPoolExecutor(max_workers=3) as executor:
        for _ in range(0,no_of_tasks):
            executor.submit(cpu_heavy)
    print(f"Runtime for serial tasks is {perf_counter()-start_time}")


