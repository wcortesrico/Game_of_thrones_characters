from .istorage import IStorage
import psycopg2
from .config import config

#Storage object is used to manage the data from PostgreSQL database
class PostgreStorage(IStorage):
    def __init__(self, params):
        self.db_params = params

    def _connect(self):
        # function to connect to the database
        try:
            connection = psycopg2.connect(**self.db_params)
            return connection
        except psycopg2.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def get_characters(self):
        # function to retrieves a list of dictionaries characters
        connection = self._connect()
        if connection:
            try:
                crsr = connection.cursor()
                crsr.execute("SELECT id, name, house, animal, symbol, nickname, role, age, death, strength FROM characters;")
                columns = [description[0] for description in crsr.description]
                characters_list = [dict(zip(columns, row)) for row in crsr.fetchall()]
                return characters_list
            except psycopg2.Error as e:
                print(f"Error fetching caracters: {e}") 
                return []
            finally:
                crsr.close()
                connection.close()

    def search_character_by_id(self, id): 
        connection = self._connect()
        if connection:
            try:
                crsr = connection.cursor()
                crsr.execute("SELECT id, name, house, animal, symbol, nickname, role, age, death, strength FROM characters WHERE id = %s;", (id,))
                columns = [description[0] for description in crsr.description]
                result = crsr.fetchone()
                if result:
                    return dict(zip(columns, result))
                else:
                    return None
            except psycopg2.Error as e:
                print(f"Error searching caracter: {e}") 
                return None
            finally:
                crsr.close()
                connection.close()

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

    def add_character(self, name, house, animal, symbol, nickname, role, age, death, strength):
        connection = self._connect()
        if connection:
            crsr = connection.cursor()
            try: 
                crsr.execute("""
                INSERT INTO characters (name, house, animal, symbol, nickname, role, age, death, strength)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id;
                """, (name, house, animal, symbol, nickname, role, age, death, strength))
                new_id = crsr.fetchone()[0]
                connection.commit()
                return new_id
            except psycopg2.Error as e:
                connection.rollback()
                print(f"Error adding character: {e}")
                return False
            finally:
                crsr.close()
                connection.close()
        return False

    def edit_character(self, id, name, house, animal, symbol, nickname, role, age, death, strength):
        connection = self._connect()
        if connection:
            crsr = connection.cursor()
            try: 
                crsr.execute("""
                UPDATE characters
                SET name=%s, house=%s, animal=%s, symbol=%s, nickname=%s, role=%s, age=%s, death=%s, strength=%s
                WHERE id=%s;
                """, (name, house, animal, symbol, nickname, role, age, death, strength, id))
                connection.commit()
                return crsr.rowcount > 0
            except psycopg2.Error as e:
                connection.rollback()
                print(f"Error editing character: {e}")
                return False
            finally:
                crsr.close()
                connection.close()
        return False

    def delete_character(self, id):
        connection = self._connect()
        if connection:
            crsr = connection.cursor()
            try:
                crsr.execute("DELETE FROM characters WHERE id=%s;", (id,))
                connection.commit()
                return crsr.rowcount > 0
            except psycopg2.Error as e:
                connection.rollback()
                print(f"Error deleting character: {e}")
                return False
            finally:
                crsr.close()
                connection.close()
        return False                   




