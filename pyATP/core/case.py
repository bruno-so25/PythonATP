from __future__ import annotations

from pathlib import Path

from ..core.section import ATPSection
from ..objects.atp_card import ATPCard


class ATPCase:
    """High-level ATP case representation.

    The case sits at the top of the library stack: it receives the ATP file,
    delegates parsing to the lower-level card model, and exposes sections as a
    semantically organized API for future expansions.
    """

    def __init__(self, filepath: str | Path):
        self.filepath = Path(filepath)
        self.card = ATPCard(str(self.filepath))
        self.sections: dict[str, ATPSection] = {}
        self._load_sections()

    def _load_sections(self) -> None:
        """Build a section map from names to lightweight ATPSection objects."""
        for section_name in self._iter_section_names():
            self.sections[section_name] = ATPSection(
                name=section_name,
                records=self._extract_section(section_name),
            )

    def _iter_section_names(self):
        return [name for name in self.card.sections.keys() if name]

    def _extract_section(self, section_name: str):
        if section_name == '/BRANCH':
            return self.card.branches
        return self.card.get_section_lines(section_name)

    def save(self, filepath: str | Path | None = None) -> str:
        """Persist the case back to disk."""
        target = Path(filepath) if filepath else self.filepath
        self.card.save(str(target))
        return str(target)

    @property
    def branches(self):
        return self.sections.get('/BRANCH', ATPSection('/BRANCH')).records

    def __repr__(self) -> str:
        return f"ATPCase(filepath={self.filepath!s}, sections={list(self.sections)})"
