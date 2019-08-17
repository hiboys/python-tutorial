import types
import sys

print(isinstance(sorted, types.BuiltinFunctionType))


is_frame = isinstance(list(sys._current_frames().values())[0], types.FrameType)

print(is_frame)


def my_func():
    pass


is_user_method = isinstance(my_func, types.FunctionType)


print(is_user_method)