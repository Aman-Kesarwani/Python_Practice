from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")

        self.opened = True
        print("Stream Opened")

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")

        self.opened = False
        print("Stream Closed")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Read data from File")


class NetworkStream(Stream):
    def read(self):
        print("Read data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Read data from memory")


print("**********************\n")

stream = MemoryStream()
stream.open()
stream.read()
stream.close()
print("**********************\n")

steam_1 = NetworkStream()
steam_1.open()
steam_1.read()
steam_1.close()

print("**********************\n")
steam_2 = FileStream()
steam_2.open()
steam_2.read()
steam_2.close()
