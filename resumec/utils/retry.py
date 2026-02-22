import time
from functools import wraps
from typing import Callable, Any

def retry_on_exception(retries: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        raise e
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator
