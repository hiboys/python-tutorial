# 最简单的 异步 http server
from aiohttp import web


async def home(request):
    return web.Response(text="hello word")


def init(address, port):
    app = web.Application()
    app.router.add_route('GET', '/', home)
    web.run_app(app, host=address, port=port)


if __name__ == "__main__":
    init("127.0.0.1", 8080)

