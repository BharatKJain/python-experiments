# Explanation

To actually run a coroutine, asyncio provides three main mechanisms:

1. The asyncio.run() function to run the top-level entry point “main()” function (see the above example.) --> coroutine-asyncio-await.py

2. Awaiting on a coroutine. --> depicted in coroutine-asyncio-await.py

3. The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks. --> depicted in coroutine-asyncio-createTask.py