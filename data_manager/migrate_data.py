import json
import psycopg2
from config import config

# Path to the JSON file
JSON_FILE_PATH = "characters.json"

def load_json_data(file_path):
    #Loads data from JSON file
    with open(file_path, "r") as new_data:
        data = json.load(new_data)
        return data

def connect_to_db():
    # Connect to the PostgreSQL database
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        return connection # extracting everything inside the params
    except psycopg2.Error as e:
        print(f"Error conecting database: {e}")

def insert_character(connection, character):
    # Insert a single character into the database
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO characters (id, name, house, animal, symbol, nickname, role, age, death, strength)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            character.get('id'),
            character.get('name'),
            character.get('house'),
            character.get('animal'),
            character.get('symbol'),
            character.get('nickname'),
            character.get('role'),
            character.get('age'),
            character.get('death'),
            character.get('strength')
        ))
        connection.commit()
        return True
    except psycopg2.Error as e:
        connection.rollback()
        print(f"Error inserting character {character.get('name')}: {e}")
        return False
    finally:
        cursor.close()

def main():
    # The Main function is to load the JSON and migrate to PostgreSQL
    characters_data = load_json_data(JSON_FILE_PATH)
    connection = connect_to_db()

    if connection:
        for character in characters_data:
            insert_character(connection, character)
        connection.close()
        print("Data migration to PostgreSQL complete!")
    else: 
        print("Data connection failed. Migration aborted.")

if __name__=="__main__":
    main()
