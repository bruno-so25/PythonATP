# pyATP/pyATP.py
from .core import ATPCase
from .objects.atp_card import ATPCard


def read_atp(filepath) -> ATPCase:
    """Load an ATP case and return the high-level case model.

    This function is the main public entry point for users who want to work
    programmatically with ATP input files. The returned object exposes the
    different sections of the case and allows editing of its data before saving.
    """
    return ATPCase(filepath)