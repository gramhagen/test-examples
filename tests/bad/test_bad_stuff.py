from examples.bad.action.stuff import Stuff


def test_do_stuff():
    cls = Stuff(path="")
    assert cls.do_stuff(1) == True
