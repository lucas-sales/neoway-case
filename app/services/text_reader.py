from abc import ABC
from app.abstracts.message_reader import MessageReaderStrategy
from app.services.dataCleaner import DataCleaner


class TextHandler(MessageReaderStrategy, ABC):
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read(self):
        data = open(self.filename, "r")
        cleaner = DataCleaner(data)
        self.data = cleaner.sanitize()
        return self.data
