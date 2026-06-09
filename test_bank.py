from bank import value


def test_value():
    assert value("hello") == 100
    assert value("hi m") == 20
    assert value("fuc u") == 0