# 使用 aiohttp 和协程 来下载

import asyncio
import aiohttp


async def fetch(base_url):
    async with aiohttp.request("GET", base_url) as response:
        if response.status == 200:
            text = await response.read()
            return text
        else:
            return None


if __name__ == "__main__":
    coroutines = []
    coroutines.append(fetch("http://www.baidu.com/"))
    coroutines.append(fetch("https://www.python.org/"))
    wait_coro =  asyncio.wait(coroutines)

    loop = asyncio.get_event_loop()
    print("start loop!")
    res, _ = loop.run_until_complete(wait_coro)

    for f in res:
        print(f.result())

    loop.close()
    print("stop loop!")


