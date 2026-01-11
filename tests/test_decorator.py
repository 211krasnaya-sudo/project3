import os
import tempfile

import pytest

from src.decorators import log, my_function


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (3, 4, 7),
        (10, 15, 25)
    ]
)
def test_log(capsys: pytest.CaptureFixture, x: int, y: int, expected: int) -> None:
    result = my_function(x, y)
    captured = capsys.readouterr()
    assert result == expected
    assert 'my_function ok' in captured.out.splitlines()[0]


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (100, "a", 18),
        (10, "d", 30)
    ]
)
def test_log_version1(capsys: pytest.CaptureFixture, x: int, y: int, expected: int) -> None:
    try:
        my_function(x, y)
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my_function ok" in captured.out
        assert isinstance(e, TypeError)


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (83, 4, 21),
        (10, 15, 11)
    ]
)
def test_log_version2(capsys: pytest.CaptureFixture, x: int, y: int, expected: int) -> None:
    if x == y:
        with pytest.raises(ValueError, match="Значения должны быть числовыми"):
            my_function(22, "c")


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (100, 1, 101),
        (10, 20, 30)
    ]
)
def test_log_version3(x: int, y: int, expected: int) -> None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        filename = temp_file.name

    decorated_function = log(filename=filename)(my_function)
    decorated_function(x, y)

    with open(filename, "r", encoding="utf-8") as file:
        log_content = file.read()
        assert "my_function ok" in log_content

    os.remove(filename)
