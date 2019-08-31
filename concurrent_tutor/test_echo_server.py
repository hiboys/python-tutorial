#简单的 echo server

import asyncio


async def handle_query(stream_reader, stream_writer):
    while True:
        data = await stream_reader.readline()
        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = '\x00'

        stream_writer.write(query.encode())
        stream_writer.write("\r\n".encode())
        await stream_writer.drain()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    host = "127.0.0.1"
    port = 8000
    server_coro = asyncio.start_server(handle_query, host, port, loop=loop)

    server = loop.run_until_complete(server_coro)

    host = server.sockets[0].getsockname()

    print('serving on {}'.format(host))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    print("server shutting down")
    server.close()

    loop.run_until_complete(server.wait_closed())
    loop.close()

