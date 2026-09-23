# pyATP/objects/atp_card.py
from __future__ import annotations

from typing import Dict, List

from .base.atp_line import ATPLine
from .components.atp_branch import BranchComponent


class ATPCard:
    """Low-level ATP file representation.

    This layer is responsible for loading the raw text and organizing it into
    logical sections without introducing business semantics. More specific
    behavior such as branch parsing lives in the component layer.
    """

    def __init__(self, filepath=None):
        self.filepath = filepath
        self.lines: List[ATPLine] = []
        self.sections: Dict[str, List[ATPLine]] = {}
        self._branch_components: List[BranchComponent] = []

        if filepath:
            self._load(filepath)
            self._parse_sections()

    def _load(self, filepath) -> None:
        """Load ATP file content while trying both common encodings."""
        tried_encodings = ['utf-8', 'latin1']
        last_exception = None

        for enc in tried_encodings:
            try:
                with open(filepath, 'r', encoding=enc) as file:
                    self.lines = [ATPLine(line) for line in file.readlines()]
                    return
            except UnicodeDecodeError as exc:
                last_exception = exc

        if last_exception is not None:
            raise last_exception
        raise ValueError(f"Could not load ATP file: {filepath}")

    def _parse_sections(self) -> None:
        """Partition the file into section buffers keyed by section name."""
        current_section = None
        buffer: List[ATPLine] = []
        self.sections = {}

        for line in self.lines:
            text = line.to_string().strip()
            if text.startswith('/'):
                if current_section is not None:
                    self.sections[current_section] = list(buffer)
                current_section = text
                buffer = []
            elif current_section:
                buffer.append(line)

        if current_section is not None:
            self.sections[current_section] = list(buffer)

        self._branch_components = self._parse_branch_components(
            self.sections.get('/BRANCH', [])
        )

    def get_section_lines(self, section_name: str) -> List[ATPLine]:
        return list(self.sections.get(section_name, []))

    def _parse_branch_components(self, lines: List[ATPLine]) -> List[BranchComponent]:
        components: List[BranchComponent] = []
        buffer: List[ATPLine] = []

        for line in lines:
            buffer.append(line)
            if line.get_field(80, 80) == '0':
                components.append(BranchComponent(buffer))
                buffer = []

        if buffer:
            components.append(BranchComponent(buffer))

        return components

    @property
    def branches(self):
        return list(self._branch_components)

    def save(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as file:
            for line in self.lines:
                file.write(line.to_string() + '\n')