from istorage import IStorage
import json

class Storage(IStorage): # Storage object is used to managed the json file; store, edit or delete items
    def __init__(self, file_path):
        self.file_path = file_path

    def get_characters(self): # this functions returns a list of characters from file
        try:
            with open(self.file_path, "r") as data_file:
                characters_list = json.loads(data_file.read())
            return characters_list
        except Exception as e:
            print(f"Error reading file: {e}")
            return False
    
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
    

    def add_character(self, name, house, animal, symbol, nickname, role, age, death, strength ):
        list_of_characters = self.get_characters()
        max_id = 0
        added = False
        for char in list_of_characters:
            if int(char["id"]) > max_id:
                max_id = char["id"]
        new_id = max_id + 1
        new_character = {
            "id": new_id,
            "name": name,
            "house": house,
            "animal": animal,
            "symbol": symbol,
            "nickname": nickname,
            "role": role,
            "age": age,
            "death": death,
            "strength": strength
        }
        list_of_characters.append(new_character)
        added = True
        if added:
            try:
                data_json = json.dumps(list_of_characters)
                with open(self.file_path, "w") as new_file:
                    new_file.write(data_json)
                    return True
            except Exception as e:
                print(f"Error writing to file: {e}")
                return False
            return False


        data_json = json.dumps(list_of_characters)
        with open(self.file_path, "w") as new_file:
            new_file.write(data_json)

    def edit_character(self, id, name, house, animal, symbol, nickname, role, age, death, strength):
        list_of_characters = self.get_characters()
        updated = False
        for char in list_of_characters:
            if int(char["id"]) == id:
                char["name"] = name
                char["house"] = house
                char["animal"] = animal
                char["symbol"] = symbol
                char["nickname"] = nickname
                char["role"] = role
                char["age"] = age
                char["death"] = death
                char["strength"] = strength
                updated = True
                break
        if updated:
            try:
                data_json = json.dumps(list_of_characters)
                with open(self.file_path, "w") as new_file:
                    new_file.write(data_json)
                    return True
            except Exception as e:
                print(f"Error writing to file: {e}")
                return False
            return False
           
    def delete_character(self, id):
        list_of_characters = self.get_characters()
        deleted = False
        for char in list_of_characters:
            if char["id"] == id:
                list_of_characters.remove(char)
                deleted = True
                break
        if deleted:
            try:
                data_json = json.dumps(list_of_characters)
                with open(self.file_path, "w") as new_file:
                    new_file.write(data_json)
                    return True
            except Exception as e:
                print(f"Error writing to file: {e}")
                return False
            return False