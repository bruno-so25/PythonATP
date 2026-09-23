# pyATP/objects/atp_card.py
from .base.atp_line import ATPLine
from .components.atp_branch import BranchComponent

class ATPCard:
    '''
    Represents an ATP input card, which contains the textual description
    of a circuit for simulation in the ATP (Alternative Transients Program).

    This class provides functionality to load, parse, and manipulate .atp
    files, preserving the fixed-column tabular format required by ATP.

    Attributes:
        filepath (str): Path to the .atp file, if provided.
        lines (list): List of ATPLine objects representing each line of the card.
    '''
    def __init__(self, filepath=None):
        '''
        Initializes the ATPCard instance.

        If a file path is provided, attempts to load the .atp file content.

        Args:
            filepath (str, optional): Path to the .atp file.
        '''
        self.filepath = filepath
        self.lines = []
        self._original_lines = []
        self._branch_components = []

        if filepath:
            self._load(filepath)
            self._parse_sections()

    def _load(self, filepath) -> None:
        '''
        Loads the .atp file into memory as a list of ATPLine objects.

        Tries UTF-8 and Latin-1 encodings. If both fail, raises the last decoding error.

        Args:
            filepath (str): Path to the .atp file to load.
        '''
        
        # Try using utf-8 and latin1 encodings
        tried_encodings = ['utf-8', 'latin1']
        last_exception = None

        for enc in tried_encodings:
            try:
                with open(filepath, 'r', encoding=enc) as file:
                    self.lines = [ATPLine(line) for line in file.readlines()]
                    return
            except UnicodeDecodeError as e:
                last_exception = e

        # If none of the encodings work, let Python raise the last error
        raise last_exception

    def _parse_sections(self):
        '''
        Identifies and parses sections like /BRANCH, mapping lines to components.
        '''
        current_section = None
        buffer = []

        for line in self.lines:
            text = line.to_string().strip()
            if text.startswith('/'):
                if current_section == '/BRANCH':
                    self._branch_components = self._parse_branch_components(buffer)
                current_section = text
                buffer = []
            elif current_section:
                buffer.append(line)

    def _parse_branch_components(self, lines):
        components = []
        buf = []
        for line in lines:
            buf.append(line)
            if line.get_field(80, 80) == '0':
                components.append(BranchComponent(buf))
                buf = []
        return components

    @property
    def branches(self):
        return self._branch_components

    def save(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for line in self.lines:
                f.write(line.to_string() + '\n')