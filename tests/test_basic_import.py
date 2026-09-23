from pyATP import ATPCase, read_atp


def test_read_atp_returns_case_object():
    case = read_atp("tests/data/sample.atp")
    assert isinstance(case, ATPCase)
    assert hasattr(case, "card")
    assert hasattr(case, "branches")
    assert len(case.branches) >= 0
