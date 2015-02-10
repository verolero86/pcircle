from abc import ABCMeta, abstractmethod

class BaseTask:
    __metaclass__ = ABCMeta

    def __init__(self, circle):
        self.circle = circle
        self.rank = circle.rank

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def process(self):
        pass


    @abstractmethod
    def reduce_init(self):
        pass

    @abstractmethod
    def reduce(self):
        pass


    @abstractmethod
    def reduce_finish(self):
        pass

    def enq(self, work):
        self.circle.enq(work)

    def deq(self):
        return self.circle.deq()


