from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def list_characters(self):
        pass
    