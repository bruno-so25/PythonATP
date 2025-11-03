# pyATP/pyATP.py
from .objects.atp_card import ATPCard
from .objects.atp_line import ATPLine

def read_atp(filepath) -> ATPCard:
    return ATPCard(filepath)