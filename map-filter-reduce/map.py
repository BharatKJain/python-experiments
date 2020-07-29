from time import perf_counter

#Without map code:
squared = []
start_time=perf_counter()
items = range(-25,25)
for i in items:
    squared.append(i**5)
print(squared)
print(f"Time consumed using loop: {perf_counter()-start_time}")
#With map code:
start_time=perf_counter()
items = range(-25,25)
squared = list(map(lambda x: x**5, items))
print(squared)
print(f"Time consumed using map: {perf_counter()-start_time}")