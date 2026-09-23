from __future__ import annotations

from typing import List

from .atp_line import ATPLine


class ATPComponent:
    """Base class for ATP domain objects.

    A component is a higher-level abstraction built from one or more ATPLine
    records. It centralizes the logic for reading and editing fixed-column
    values without tying this behavior to a specific ATP section.
    """

    def __init__(self, lines: List[ATPLine]):
        self.lines = lines

    def get_field(self, start: int, end: int, line: int = 0):
        return self.lines[line].get_field(start, end)

    def set_field(self, start: int, end: int, value: str, line: int = 0):
        self.lines[line].set_field(start, end, value)

    def __iter__(self):
        return iter(self.lines)
