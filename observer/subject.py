# observer/subject.py
from abc import ABC, abstractmethod

class Subject(ABC):
    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        """Attach an observer to the subject."""
        self.observers.add(observer)
    
    def detach(self, observer):
        """Detach an observer from the subject."""
        self.observers.remove(observer)

    def notify(self):
        """Notify all attached observers."""
        for observer in self.observers:
            observer.update()

    @abstractmethod
    def get_state(self):
        """Get the current state of the subject."""
        pass

    @abstractmethod
    def set_state(self, state):
        """Set the state of the subject."""
        pass