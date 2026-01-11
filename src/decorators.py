from functools import wraps
from typing import Any, Callable


def log(filename: str | None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для логирования"""

    def decorator(func: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\nРезультат: {result}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)

        return wrapper

    return decorator


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    return x + y
