from abc import ABC, abstractmethod
class ImethodStacks(ABC):
    @abstractmethod
    def push(self, element):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def count(self):
        pass
