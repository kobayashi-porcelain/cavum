import os
import pytest
from cavum.core.elf_parser import ELFParser

@pytest.fixture
def elf_binary_path():
    return os.path.join(os.path.dirname(__file__), '..', 'assets', 'hello')

def test_elf_parser_loads_symbols(elf_binary_path):
    parser = ELFParser(elf_binary_path)
    parser.load()

    # Should contain main, my_func, and possibly others
    assert 'main' in parser.symbols
    assert 'my_func' in parser.symbols
    assert isinstance(parser.get_symbol_addr('main'), int)
    assert isinstance(parser.get_symbol_addr('my_func'), int)
