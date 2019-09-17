# 三种描述符


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    """带有一个 name，然后其他参数都放到 args 里面了"""
    pseudo_args = ','.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    """覆盖型描述符有 get set 方法"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class Managed:
    over = Overriding()


if __name__ == "__main__":
    # 通过类来访问描述符，会调用 get 方法，这个时候 instance 是None 值
    print(Managed.over)
