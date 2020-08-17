from abc import ABC, ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def printArea(self):
        return 0


class Test(AbstractClass):
    pass
