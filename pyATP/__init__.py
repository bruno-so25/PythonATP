# pyATP/__init__.py

__author__ = 'Bruno Oliveira'
__email__ = 'bruno.sowk@gmail.com'

from .core import ATPCase, ATPSection
from .pyATP import read_atp

__all__ = ["ATPCase", "ATPSection", "read_atp"]