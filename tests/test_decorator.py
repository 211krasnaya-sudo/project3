
from src.decorators import log, my_function
import pytest


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (3, 4, 7),
        (10, 15, 25)
    ]

)
def test_log(capsys, x, y, expected):
    result = my_function(x, y)
    captured = capsys.readouterr()
    assert result == expected
    assert 'my_function ok' in captured.out.splitlines()[0]

# parametrize = [
#     {"x": 3, "y": 4, "expected": 7},
#     {"x": 10, "y": 15, "expected": 25}
# ]
#
# for param in parametrize:
#     test_log(**param)
