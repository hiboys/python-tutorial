import abc


class A(abc.ABC):

    @abc.abstractmethod
    def ping(self):
        pass


if __name__ == "__main__":
    a = A()

