# Setting Up the PostgreSQL Database for the Game if Thrones Characters App

This Document outlines the steps required to set up the PostgreSQL database for the Flask application.

## Prequisites

- **PostgreSQL installed:** Ensure you have PostgreSQL installed on your system. You can download it from the official PostgreSQL website: [https://www.postgresql.org/download/] (https://www.postgresql.org/download/)
- **psycopg2:** This python library is required to interact with PostgreSQL. it should be installed in your project's enviroment. If not, you can install it using pip:
```bash
pip install psycopg2-binary
```

## Database configuration
The application uses a `database.ini` file to store the PostgreSQL connection parameters. this file should be locatated in the same directory as your `config.py` file (likely the root of your project).

**Contents of `database.ini`:**

```ini
[postgresql]
host=localhost
database=GoT_characters
user=postgres
password=Postgrespassword
```

## Important:

- Adjust Credentials: Modify the host, database, user, and password values in database.ini to match your PostgreSQL server configuration.

- Database Creation: Ensure that the database specified in the database.ini file (GoT_characters in this case) exists on your PostgreSQL server. You can create it using a PostgreSQL administration tool (like pgAdmin) or the psql command-line interface:

SQL
```ini
CREATE DATABASE GoT_characters;
```



## Database Schema
The application expects a table named characters with the following schema:

SQL
```ini
CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name TEXT,
    house TEXT,
    animal TEXT,
    symbol TEXT,
    nickname TEXT,
    role TEXT,
    age INTEGER,
    death TEXT,
    strength INTEGER
);
```

You can execute this SQL statement using a PostgreSQL administration tool or the psql command-line interfce connected to your GoT_characters database. 

## Explanation of the Schema: 
- id SERIAL PRIMARY KEY: This creates an auto-incrementing integer column that serves as the unique identifier for each character. SERIAL automatically creates an underlying sequence.

- name TEXT: The name of the character.

- house TEXT: The house the character belongs to.

- animal TEXT: The character`s associated animal (e.g., direwolf).

- symbol TEXT: The symbol or sigil of the character or their house.
- nickname TEXT: The character`a nickname or alias.

- role TEXT: The character`s role or title.

- age INTEGER: The character`s age (can be NULL).

- death TEXT: Information about the character`s death (can be NULL or a description).

- strength INTEGER: A numerical representation of the character`s strength or power (can be NULL).

## Migrating Data(Seeding the Database)

The project includes a migrate_data.py script to populate the characters table with data from the characters.json file located in the data_manager directory.

Steps to Migrate Data:

1. Ensure characters.json Exists: Verify that the data_manager/characters.json file contains the character data in JSON format.

2. Run the Migration Script: Execute the migrate_data.py script from your project`s root directory:
```bash
python data_manager/migrate_data.py
```

This script will:

- Read the database connection parameters from database.ini.

- Connect to the GoT_characters PostgreSQL database.

- Read the data from data_manager/characters.json.

- Insert each character as a new row into the characters table.

- Print a confirmation message upon completion or any errors encountered.


## Important Notes:

- Initial Data: The migrate_data.py script assumes that the characters table might be empty or that you want to re-populate it. If you run it multiple times, it will attempt to insert the same data again. If the id values in your characters.json already exist in the database, you might encounter primary key constraint violations. Consider dropping the table or ensuring unique IDs in your JSON data if you need to run the migration multiple times.

- SERIAL and Initial Data: The migrate_data.py script in its current form explicitly inserts the id from the characters.json file. If you want to fully leverage the SERIAL functionality and let PostgreSQL generate the IDs during the initial data load, you would need to modify the insert_character function in migrate_data.py to omit the id column from the INSERT statement. However, if your characters.json already contains specific IDs that you want to preserve, the current script will work.

## Running Flask Application

Once the database is set up and data is migrated, you can run the Flask application (app.py)
```bash
python app.py
```

The application will be accesible at "http://localhost:5000/characters

By following these steps, reviewers should be able to easyíly set up the PostgreSQL database and run the application. 