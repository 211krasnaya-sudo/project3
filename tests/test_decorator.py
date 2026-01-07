
from src.decorators import log, my_function
import pytest

@log
def test_log(capsys):
    my_function(3, 4)
    captured = capsys.readouterr()
    assert captured.out.splitlines()[0] == "Имя функции: my_function"


