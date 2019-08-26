# 熟悉有限队列的使用
# 熟悉生成器的使用

from collections import deque


def search(lines, pattern, max_history_line = 5):
    history_lines = deque(maxlen=max_history_line)
    for line in lines:
        if pattern in line:
            yield line, history_lines
            history_lines.append(line)


if __name__ == "__main__":

    with open("lines.txt", "r") as f:
        for current_line, previous_lines in search(f, "hello"):
            print("history_lines:")
            print(previous_lines)
            print("current_line:")
            print(current_line)

