"""
This module demonstrate.

    Author: Bharat Kumar Jain
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import perf_counter
import sys


def cpu_heavy():
    try:
        raise Exception("Check the variable name")
        # count = 0
        # for i in range(10**6):
        #     count += i
    except Exception as err:
        print(err)
        sys.exit()


if __name__ == "__main__":
    try:
        no_of_tasks = 3
        with ProcessPoolExecutor(max_workers=3) as executor:
            for _ in range(0, no_of_tasks):
                executor.submit(cpu_heavy)
    except Exception as err:
        
