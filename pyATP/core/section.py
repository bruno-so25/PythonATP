from __future__ import annotations


class ATPSection:
    """Represents a logical section in an ATP case.

    This is intentionally a lightweight abstraction that allows the library to
    evolve toward richer section-level semantics without locking the API too
    early.
    """

    def __init__(self, name: str, records=None):
        self.name = name
        self.records = list(records or [])

    def add_record(self, record):
        self.records.append(record)

    def __iter__(self):
        return iter(self.records)

    def __len__(self):
        return len(self.records)
