# Explanation
Represents the basic time difference between code execution of synchronous code and asynchronous code in python

Checkout this URL: https://realpython.com/async-io-python/


Code Explanation:

perf_counter() function always returns the float value of time in seconds.(https://www.geeksforgeeks.org/time-perf_counter-function-in-python/)

The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”


For understanding coroutines: https://docs.python.org/3/library/asyncio-task.html