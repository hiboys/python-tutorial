

class StrKeyDict(dict):

    def __missing__(self, key):
        # 这个判断防止递归
        if  isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default = None):

        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        # 为了保持一致性，所以需要这个方法
        # 这个在 python 中是很快的，因为 keys 返回的是一个视图
        return item in self.keys() or str(item) in self.keys()

