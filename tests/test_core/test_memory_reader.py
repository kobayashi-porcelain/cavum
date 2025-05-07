import pytest
from cavum.core.memory_reader import MemoryReader
import os

TEST_DUMP = os.path.join(os.path.dirname(__file__), "test_data", "dummy.bin")

def setup_module(module):
    # Create a small dummy binary file for testing
    os.makedirs(os.path.dirname(TEST_DUMP), exist_ok=True)
    with open(TEST_DUMP, "wb") as f:
        f.write(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # 26 bytes

def teardown_module(module):
    os.remove(TEST_DUMP)

def test_read_within_bounds():
    reader = MemoryReader(TEST_DUMP)
    data = reader.read(0, 5)
    assert data == b"ABCDE"
    assert reader.size == 26

def test_read_out_of_bounds():
    reader = MemoryReader(TEST_DUMP)
    with pytest.raises(IndexError):
        reader.read(25, 5)  # only 1 byte at offset 25
