import struct

class Packet:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def get(self, length: int) -> bytes:
        if self.pos + length > len(self.data):
            raise ValueError("packet overflow")
        
        start = self.pos
        self.pos += length
        return self.data[start:self.pos]

    def read(self, fmt: str):
        size = struct.calcsize(fmt)
        return struct.unpack(fmt, self.get(size))[0]
