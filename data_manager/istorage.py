from abc import ABC, abstractmethod

# Creating the abstract methods for functions that interacts directly with the json file
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

    


    