from api.index import getGlobalsFromModule

"""
Test the function that removes all the __xyz__ names
"""
def test_getGlobalsFromModule():
    # Normal case
    a = ["__name__", "__all__", "myVar"]
    b = getGlobalsFromModule(a)

    assert len(b) == 1
    assert b == ["myVar"]

    # All must be removed case
    c = ["__name__", "__all__"]
    d = getGlobalsFromModule(c)
    assert len(d) == 0
    assert d == []

    # Edge case 1 - where only the name starts with double underscores
    e = ["__name__", "__all"]
    f = getGlobalsFromModule(e)
    assert len(f) == 1
    assert f == ["__all"]

    # Edge case 2 - where only the name ends with double underscores
    g = ["__name__", "all__"]
    h = getGlobalsFromModule(g)
    assert len(h) == 1
    assert h == ["all__"]
