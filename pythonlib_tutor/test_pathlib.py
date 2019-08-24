#新增目录 ok
#递归穿甲目录 ok
#删除目录 ok
#新增文件 ok
#写文件 ok
#删除文件 ok
#拷贝文件 ok
#判断文件是否存在 ok
#列出一个目录下有什么文件 ok
#获取一个文件的决定路径 ok

import os
import shutil
import pathlib


demo_path = pathlib.Path("demo")
if demo_path.exists() is False:
    # 创建目录
    demo_path.mkdir()

# 递归删除目录
# shutil.rmtree(demo_path)


demo_path = pathlib.Path("demo/test.txt")
demo_path.write_text("hello world")

# 读取文件
hello_word = demo_path.read_text();
print(hello_word)

if demo_path.exists():
    # 删除文件
    # os.remove(demo_path)
    target_path = pathlib.Path("demo2/deeper/test2.txt");
    if target_path.parent.exists() is False:
        # 递归创建目录
        os.makedirs(target_path.parent)
    # 拷贝文件
    shutil.copyfile(demo_path, target_path)

    # 列出一个目录下的所有文件
    dir_files = target_path.parent.rglob("*")
    print(list(dir_files))

    # 获取一个文件的状态
    stat = target_path.stat()
    print(stat)

    # 获取一个文件的决定路径
    # 简单
    print(target_path.absolute())

    print(target_path.parent.joinpath("test3.txt"))
