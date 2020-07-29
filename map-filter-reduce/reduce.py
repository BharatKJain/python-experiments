from functools import reduce
from time import perf_counter
#Without using reduce:
start_time= perf_counter()
product = 1
list_num = range(1,12)
for num in list_num:
    product = product * num
print(product)
print(f"Time consumed by looping: {perf_counter()-start_time}")
#With using reduce:
start_time= perf_counter()
product = reduce((lambda x, y: x * y), list_num)
print(product)
print(f"Time consumed by looping: {perf_counter()-start_time}")