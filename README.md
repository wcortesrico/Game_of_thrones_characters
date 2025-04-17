# Game of Thrones Characters Application

This application allows users to browse, search, filter, add, edit and delete characters from Game of Thrones

## Brief Description
This application is built using python and Flask microframework. 

* **Model (Storage):** The 'storage_json.py' file implements the 'IStorage' interface and manages character data stored in a JSON file ('characters.json'). It provides functions to read, search, filter, add, edit and delete character information. 
* **View (templates):** the 'templates' directory contains HTML files that are rendered using the Jinja2 templating engine to display character data and provide user interface for various functionalities. 
* **Controller (Flask Routes):** The 'app.py' file defines the routes and logic to handle HTTP requests, interact with the 'Storage' class, and render the appropiate HTML templates. It includes functionalities for pagination, searching, filtering, adding, editing and deleting characters. 

The application provides a web interface for users to interact with the Game of Thrones character data

## Assumptions

While developing this application, I made the following assumptions

* **Data Storage:** Character data is stored in a JSON file mamed 'character.json' in the application's root directory.
* **Character Structure:** Each character in the JSON file is a dictionary with keys like 'id', 'name', 'house', 'animal', 'symbol', 'nickname', 'role', 'age', 'death', and 'strenght'.
* **Unique IDs:** Each character has a unique 'id'.
* **Filtering:** Filtering is based on exact matches for the selected attributes values.
* **Pagination:** Pagination is implemented with default random display of 20 characters if 'limit' and 'skip' parameters are not provided. Users can specify 'limit' and 'skip' for more controlled pagination.
* **Sorting:** Sorting is implemented based on a selected attribute ('sort_by') and order ('order=sort_asc' or 'order=sort_des').
* **Error Handling:** Basic error handling for "Character not Found" during search and edit operations is included.

## Setup Instructions

To set up the application on your local machine, follow the steps:

1. **Prerequisites:**
   * **Python 3.x** installed on your system. 
   * **pip** (Python package installer) should be included with your python installation. 

2. **Clone the Repository:**
    ```bash
    git clone https://github.com/wcortesrico/Game_of_thrones_characters.git
    cd Game_of_Thrones_Characters
    ```
3. **Install Dependencies:**
   ```bash
   pip install Flask
   ```

4. **Create Data File:**
    Ensure you have a JSON file named 'characters.json' in your project's root directory containing the character data. The structure should be at list of character dictionaries as assumed in the "Assumptions" section. 

## Running the Server

To start the Flask development server, navigate to your project's directory in your terminal and run the following command:

```bash
python app.py
```

Once the server starts, you should see output indicating the server is running (tipically on 'http://127.0.0.1:500/'). Open your web browser and go to this address to acces the application. 

## API Endpoints 

1. Endpoint: "/characters or /characters/page/<page>" 	
   HTTP Method: GET
   Description: Displays a list of Game of Thrones characters with pagination.
   Usage: Open "http://127.0.0.1:5000/characters" in your browser for a random selection (up to 20). Use "http://127.0.0.1:5000/characters?limit=<count>&skip=<offset>" for specific pagination. For page numbers, use "http://127.0.0.1:5000/characters/page/<number>?limit=<count>&skip=<offset>".

2. Endpoint: "/characters/search?search=<id>"
   HTTP Method: GET
   Description:	Searches for a character by their ID.
   Usage: Open "http://127.0.0.1:5000/characters/search?search=<character_id>" in your browser, replacing "<character_id>" with the ID of the character you want to find.

3. Endpoint: /characters/filters
   HTTP Method: GET
   Description:	Displays a page with filtering options for character attributes.
   Usage: Open "http://127.0.0.1:5000/characters/filters" in your browser. Use checkboxes to select attribute values and click "Apply Filters". You can also use query parameters directly in the URL (e.g., "http://127.0.0.1:5000/characters/filters?house=Stark&role=Lord+Commander&sort_by=name&order=sort_asc&age_more_than=20&age_less_than=40)".
   
4. Endpoint: "/characters/add_character"
   HTTP Method:	GET
   Description: Displays a form to add a new character.
   Usage: Open "http://127.0.0.1:5000/characters/add_character" in your browser.

5. Endpoint: "/characters/add_character"
   HTTP Method:	POST
   Description:	Adds a new character to the data store.	
   Usage: Submit the form displayed at the GET endpoint with the details of the new character.

6. Endpoint: "/characters/edit_character/<id>"
   HTTP Method:	GET
   Description:	Displays a form to edit the details of a specific character.
   Usage: Open "http://127.0.0.1:5000/characters/edit_character/<character_id>" in your browser, replacing "<character_id>" with the ID of the character you want to edit.

7. Endpoint: "/characters/edit_character/<id>"
   HTTP Method:	POST
   Description:	Updates the details of a specific character in the data store.
   Usage: Submit the form displayed at the GET endpoint with the updated values for the character.

8. Endpoint: "/characters/delete_character/<id>"	
   HTTP Method: GET	
   Description: Displays a confirmation page before deleting a specific character.	
   Usage: Click the "Delete character" button on the home page for a specific character.
   Usage: This will navigate you to a confirmation page at this URL.

9. Endpoint: "/characters/delete_character/<id>"	
   HTTP Method: POST	
   Description: Deletes a specific character from the data store after confirmation.
   Usage: Click the "Confirm Delete" button on the confirmation page displayed at the GET endpoint.
   

## Usage Examples
Here are some examples of how to use the application through your web browser

- Browsing Characters (First Page, Default): Open "http://127.0.0.1:5000/characters" or "http://127.0.0.1:5000/characters/page/1".

- Browsing Characters (Page 3, Limit 10): Open "http://127.0.0.1:5000/characters/page/3?limit=10".

- Searching for Character with ID 5: Open "http://127.0.0.1:5000/characters/search?search=5".

- Filtering Characters from House Stark: Open "http://127.0.0.1:5000/characters/filters?house=Stark".

- Filtering Characters who are Lord Commander: Open "http://127.0.0.1:5000/characters/filters?role=Lord+Commander".

- Filtering Characters older than 30: Open "http://127.0.0.1:5000/characters/filters?age_more_than=30".

- Filtering and Sorting (Stark characters, sorted by name ascending): Open "http://127.0.0.1:5000/characters/filters?house=Stark&sort_by=name&order=sort_asc".

- Adding a New Character: Navigate to "http://127.0.0.1:5000/characters/add_character" and fill out the form.

- Editing Character with ID 2: Click the "Edit character" button next to the character with ID 2 on the home page, or directly open "http://127.0.0.1:5000/characters/edit_character/2".

- Deleting Character with ID 1: Click the "Delete character" button next to the character with ID 1 on the home page and then click "Confirm Delete" on the confirmation page.

