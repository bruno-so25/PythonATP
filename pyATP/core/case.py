from __future__ import annotations

from pathlib import Path

from ..objects.atp_card import ATPCard


class ATPCase:
    """High-level ATP case representation.

    This object is intended to be the public model used by users who want to
    load an ATP case, inspect its sections, modify values programmatically and
    save the result back to disk.
    """

    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)
        self.card = ATPCard(str(self.filepath))
        self.sections = {}
        self._load_sections()

    def _load_sections(self) -> None:
        """Organize the parsed card into high-level sections.

        The current implementation builds a simple mapping from section names to
        the underlying component list. This is intentionally lightweight so the
        public API is easy to evolve without changing the lower-level parser.
        """
        for section_name in self._iter_section_names():
            self.sections[section_name] = self._extract_section(section_name)

    def _iter_section_names(self):
        names = []
        for line in self.card.lines:
            text = line.to_string().strip()
            if text.startswith('/'):
                names.append(text)
        return names

    def _extract_section(self, section_name: str):
        return [
            component
            for component in self.card.branches
            if component is not None
        ]

    def save(self, filepath: str | Path | None = None) -> str:
        """Persist the case back to disk."""
        target = Path(filepath) if filepath else self.filepath
        self.card.save(str(target))
        return str(target)

    @property
    def branches(self):
        return self.card.branches

    def __repr__(self) -> str:
        return f"ATPCase(filepath={self.filepath!s}, sections={list(self.sections)})"
