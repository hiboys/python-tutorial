# 使用 ThreadPoolExecutor 进行简单的并发处理


from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
import threading


def my_print(n):
    return str(n) + " " + str(threading.currentThread().ident)


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as executor:
        fs = []
        for i in range(10):
            f = executor.submit(my_print, i)
            fs.append(f)

        for r in futures.as_completed(fs):
            print(r.result())






