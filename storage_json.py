from istorage import IStorage
import json

class Storage(IStorage): # Storage object is used to managed the json file; store, edit or delete items
    def __init__(self, file_path):
        self.file_path = file_path

    def get_characters(self): # this functions returns a list of characters from file
        with open(self.file_path, "r") as data_file:
            characters_list = json.loads(data_file.read())
        return characters_list
    
    def search_character_by_id(self, id): #  Function to return a character from specific Id
        list_characters = self.get_characters()
        for character in list_characters:
            if id == int(character["id"]):
                return character
            
    # this functions returns a list of all attributes names
    def get_all_attributes_title(self):
        list_characaters = self.get_characters()
        titles = []
        for character in list_characaters: 
            for title in character.keys():
                if title not in titles:
                    titles.append(title)
        titles.remove("id")
        titles.remove("age")     
        titles.remove("name")       
        return titles
    
    # this functions returns a list of all atributes values
    def get_all_attributes(self):
        list_characaters = self.get_characters()
        attributes = []
        for character in list_characaters:
            for attribute in character.values():
                if attribute not in attributes:
                    attributes.append(attribute)
        return attributes
    
    # this function returns a dictionary with the attributes as keys and the values as a list
    def get_attributes_dictionary(self):
        all_characters = self.get_characters()
        all_attributes = self.get_all_attributes()
        all_titles = self.get_all_attributes_title()
        attributes = {}
        for title in all_titles:
            temp = []
            for character in all_characters:
                for attribute in all_attributes:
                    if character[title] == attribute and attribute not in temp:
                        temp.append(attribute)
                    attributes[title] = temp
        return attributes
    
    # this function retrieves a list of characters fitered according to their attributes
    def filter_char(self, filters): # the variable filters spected as a dictionary of attributes
        list_characters = self.get_characters()
        filtered =[]
        for char in list_characters: 
            for attribute, values in filters.items():
                for value in values:
                    if char[attribute] == value:
                        filtered.append(char)
        return filtered