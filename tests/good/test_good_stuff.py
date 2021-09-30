from examples.good.action.stuff import Stuff


def test_do_stuff(mock_model):
    cls = Stuff(model=mock_model)
    assert cls.do_stuff(1) == True
    mock_model.predict.assert_called_once_with(data=2)
