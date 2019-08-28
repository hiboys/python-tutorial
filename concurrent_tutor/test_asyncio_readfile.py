# 从标准输入读取数据，并且打印

import asyncio
import sys


loop = asyncio.get_event_loop()


def read_file(*args):
    line = sys.stdin.readline()
    print(line)


if __name__ == "__main__":
    loop.add_reader(sys.stdin.fileno(), read_file)
    loop.run_forever()
