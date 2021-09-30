from unittest.mock import patch
from examples.bad.action.stuff import Stuff


def test_do_stuff():
    with patch("examples.bad.action.stuff.Model") as MockModel:
        # You can adjust nested return values for MagicMocks
        # don't use MockModel() syntax like line 13, otherwise assert_called_once will fail
        MockModel.return_value.predict.return_value = True
        cls = Stuff(path="")
        assert cls.do_stuff(1) == True
        MockModel.assert_called_once_with(path="")
        MockModel().predict.assert_called_once_with(data=2)
