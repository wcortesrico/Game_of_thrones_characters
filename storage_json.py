from istorage import IStorage
import json

class Storage(IStorage): # Storage object is used to managed the json file; store, edit or delete items
    def __init__(self, file_path):
        self.file_path = file_path

    def get_characters(self): # this functions returns a list of characters from file
        with open(self.file_path, "r") as data_file:
            characters_list = json.loads(data_file.read())
        return characters_list


