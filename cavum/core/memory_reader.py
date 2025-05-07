class MemoryReader:
    """
    Provides simple read access to a raw memory dump file.
    """

    def __init__(self, path: str):
        self.path = path
        with open(path, "rb") as f:
            self._data = f.read()
        self.size = len(self._data)

    def read(self, offset: int, size: int) -> bytes:
        """
        Read `size` bytes from the dump, starting at `offset`.
        Raises IndexError if out of bounds.
        """
        if offset < 0 or offset + size > self.size:
            raise IndexError(f"Attempt to read outside of bounds: offset={offset}, size={size}")
        return self._data[offset : offset + size]