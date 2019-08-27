# 使用 ThreadPoolExecutor 进行简单的并发处理

from concurrent.futures import ThreadPoolExecutor
import threading


def my_print(n):
    print(n, threading.currentThread().ident)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(my_print, range(10))


