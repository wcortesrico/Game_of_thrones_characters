from abc import ABC, abstractmethod

class IStorage(ABC):
    @abstractmethod
    def get_characters(self):
        pass

    @abstractmethod
    def add_character(self):
        pass

    @abstractmethod
    def edit_character(self):
        pass

    @abstractmethod
    def delete_character(self):
        pass

    


    