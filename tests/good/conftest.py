from unittest.mock import MagicMock
import pytest


@pytest.fixture(scope="module")
def mock_model():
    mock_model = MagicMock()
    mock_model.predict.return_value = True
    return mock_model
