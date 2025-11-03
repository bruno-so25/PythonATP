# pyATP/objects/atp_component.py
from .atp_line import ATPLine

class ATPComponent:
    """
    Base class for all ATP components.
    Wraps one or more ATPLine instances and provides utilities to access fields by column.
    """
    def __init__(self, lines: list[ATPLine]):
        self.lines = lines

    def get_field(self, start: int, end: int, line: int = 0):
        return self.lines[line].get_field(start, end)

    def set_field(self, start: int, end: int, value: str, line: int = 0):
        self.lines[line].set_field(start, end, value)