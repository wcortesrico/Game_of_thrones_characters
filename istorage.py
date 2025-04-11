from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def get_characters(self):
        pass
    