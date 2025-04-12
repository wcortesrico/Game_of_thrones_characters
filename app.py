from flask import Flask, request, redirect, url_for, render_template
from storage_json import Storage
import math
import random

storage = Storage("characters.json")

app = Flask(__name__)


@app.route('/characters')
@app.route('/characters/page/<int:page>')
def home(page=1):
    list_of_characters = storage.get_characters()
    total_characters = len(list_of_characters)

    limit = request.args.get('limit', default=None, type=int)
    skip = request.args.get('skip', default=0, type=int )
    list_of_characters = list_of_characters[skip : ] # creating the list whit skipped characters
    
    # Returning random list when limit and skip are not defined
    if limit == None and skip == 0:
        if len(list_of_characters) <= 20:
            random_characters = list_of_characters
        else:
            random_characters = random.sample(list_of_characters, 20)
        return render_template('home.html',
                               characters=random_characters,
                               page=0,
                               total_pages=0)
    
    # rerturning the list with the skipped characters
    elif skip > 0 and limit == None:
        print(len(list_of_characters))
        return render_template('home.html',
                               characters=list_of_characters,
                               limit=limit,
                               page=0,
                               total_pages=0,
                               skip=skip)

    # returning pagination list in each page
    else:
        total_pages = math.ceil(total_characters/limit) # calculating total number of pages

        # Ensure the requested page is between the number of pages
        if page < 1:
            return redirect(url_for('home', page=1, limit=limit, skip=skip))
        elif page > total_pages and total_pages > 0:
            return redirect(url_for('home', page=total_pages, limit=limit, skip=skip))
        
        # calculate the first character based on the current page
        first_char = (page - 1) * limit
        characters_per_page = list_of_characters[first_char : first_char + limit] 
        return render_template('home.html',
                               characters=characters_per_page,
                               page=page, total_pages=total_pages,
                               limit=limit, skip=skip)


@app.route('/characters/search') # endoint to return a character searched by Id
def search_by_id():
    id = request.args.get("search")
    character_searched = storage.search_character_by_id(int(id)) # Using the function from Storage to get the character
    if character_searched == None:
        return "No Character found"
    return render_template('search.html', character=character_searched)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
