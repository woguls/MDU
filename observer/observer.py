# observer/observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self):
        """Update method to be called by the subject."""
        pass
