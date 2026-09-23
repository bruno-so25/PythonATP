class ATPLine:
    """Represents a single ATP line preserving fixed-column formatting."""

    def __init__(self, raw_line: str):
        self.raw_line = raw_line.rstrip("\n")
        self.columns = self._to_column_dict(self.raw_line)

    def _to_column_dict(self, line: str) -> dict:
        return {i + 1: c for i, c in enumerate(line.ljust(80))}

    def to_string(self) -> str:
        return "".join(self.columns.get(i, " ") for i in range(1, 81))

    def get_field(self, start: int, end: int) -> str:
        return "".join(self.columns.get(i, " ") for i in range(start, end + 1)).strip()

    def set_field(self, start: int, end: int, value: str):
        value = value.rjust(end - start + 1)[: end - start + 1]
        for i, c in enumerate(value, start=start):
            self.columns[i] = c
        self.raw_line = self.to_string()

    def __str__(self):
        return self.to_string()
