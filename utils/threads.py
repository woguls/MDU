#utils/threads.py

from PyQt6.QtCore import  QMutex
from functools import wraps

def thread_safe_method(mutex_name):
    """Allows mutexes to use the context manager protocol"""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            mutex : QMutex = getattr(self, mutex_name, None)
            if mutex:
                mutex.lock()
                try:
                    return func(self, *args, **kwargs)
                finally:
                    mutex.unlock()
            else:
                raise AttributeError(f"Mutex {mutex_name} not found in {self.__class__.__name__}")
        return wrapper
    return decorator
