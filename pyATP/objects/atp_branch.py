# pyATP/objects/atp_branch.py
from .atp_component import ATPComponent

class BranchComponent(ATPComponent):
    """
    Represents a component from the /BRANCH section of the ATP file.
    Each component may span multiple lines, and provides access to common fields.
    """
    @property
    def type(self):
        return self.get_field(0, 1)
    
    @property
    def n1(self):
        return self.get_field(3, 8)

    @property
    def n2(self):
        return self.get_field(9, 14)

    @property
    def resistance(self):
        return self.get_field(27, 32)

    @resistance.setter
    def resistance(self, value):
        self.set_field(27, 32, value)