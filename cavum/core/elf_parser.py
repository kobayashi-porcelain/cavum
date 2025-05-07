from typing import Optional, Dict
import logging

from elftools.elf.elffile import ELFFile  # <-- Correct direct import
from elftools.elf.constants import SHN_INDICES  # Optional, for future use

ELF_MAGIC = b'\x7fELF'

log = logging.getLogger(__name__)

class ELFParser:
    def __init__(self, path: str):
        self.path = path
        self.symbols: Dict[str, int] = {}

    def load(self) -> None:
        with open(self.path, 'rb') as f:
            if f.read(4) != ELF_MAGIC:
                raise ValueError("Not a valid ELF file.")
            f.seek(0)
            self._parse(f)

    def _parse(self, f) -> None:
        elf = ELFFile(f)

        symtab = elf.get_section_by_name('.symtab')
        if not symtab:
            raise ValueError("Symbol table (.symtab) not found.")

        for symbol in symtab.iter_symbols():
            if symbol['st_info']['type'] in ('STT_OBJECT', 'STT_FUNC'):
                self.symbols[symbol.name] = symbol['st_value']

    def get_symbol_addr(self, name: str) -> Optional[int]:
        return self.symbols.get(name)
