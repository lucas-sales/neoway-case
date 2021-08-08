from abc import ABC, abstractmethod


class MessageReaderStrategy(ABC):

    @abstractmethod
    def read(self):
        pass
