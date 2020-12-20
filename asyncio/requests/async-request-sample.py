# article: https://stackoverflow.com/questions/49869769/how-do-i-properly-run-an-asyncio-aiohttp-request-in-a-loop

###############
#
# Asynchronous code in python
#
###############
import asyncio
import aiohttp
from time import perf_counter
import requests

lists = ['ethereum', 'bitcoin', 'xmr', 'req', 'xlm', 'etc',
         'omg', 'neo', 'btc', 'xmr', 'req', 'xlm', 'etc', 'omg', 'neo']


async def fetch(client, item):
    url = 'https://coincap.io/{endpoint}/{coin_name}'.format(
        endpoint='assets',
        coin_name=item.upper()
    )
    async with client.get(url) as resp:
        assert resp.status == 200
        html = await resp.text()
        print(item)


async def main():
    async with aiohttp.ClientSession() as client:
        await asyncio.gather(*[
            asyncio.ensure_future(fetch(client, item))
            for item in lists
        ])

start = perf_counter()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(f"Total time for ayncio: {perf_counter()-start}")

#################################################################################
#
# Regular python requests code:
#
#################################################################################
start = perf_counter()
for item in lists:
    response=requests.get('https://coincap.io/{endpoint}/{coin_name}'.format(
        endpoint='assets',
        coin_name=item.upper()
    ))
    print(item)
print(f"Total time for requests: {perf_counter()-start}")
