from rebanking import value


def test_rebanking():
    assert value("Hey") == "$20"
    assert value("How you doing?") == "$20"
    assert value("How's it going?") == "$20"
    assert value("What's happening?") == "$100"
    assert value("What's up?") == "$100"
