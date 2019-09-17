
def my_print(*args, **kwargs):
    print("args values:")
    for arg in args:
        print(arg)

    print("\n")

    print("kargs values:")
    for k, v in kwargs.items():
        print(k, v)


if __name__ == "__main__":
    my_print(1, 2, 3, a=4, b=5)
