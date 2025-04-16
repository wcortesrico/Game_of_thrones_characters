from flask import Flask, request, redirect, url_for, render_template
from storage_json import Storage
import math
import random

storage = Storage("characters.json")

app = Flask(__name__)


# this function retrieves a list of characters fitered according to their attributes
def filter_char(list_characters, filters): # the variable filters expected as a dictionary of attributes
    filtered =[]
    for char in list_characters: 
        for attribute, values in filters.items():
            for value in values:
                if char[attribute] == value:
                    filtered.append(char)
    return filtered

# function that retrieves a list of characters sorted according to attribute and ordered
def sorting_by(char_list, sort_by, order):
    sorted_list = []
    values_list = []
    for char in char_list:
        if char[sort_by] != None:
            values_list.append(char[sort_by])
    values_list.sort()
    if order == "sort_des":
        values_list.sort(reverse=True)
    for value in values_list:
        for char in char_list:
            if char[sort_by] == value:
                sorted_list.append(char)
    return sorted_list


@app.route('/characters')
@app.route('/characters/page/<int:page>')
def home(page=1):
    list_of_characters = storage.get_characters()
    total_characters = len(list_of_characters)
    all_attributes = storage.get_attributes_dictionary()

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
                               total_pages=0,
                                attributes=all_attributes,
                                selected_filters={})
    
    # rerturning the list with the skipped characters
    elif skip > 0 and limit == None:
        print(len(list_of_characters))
        return render_template('home.html',
                               characters=list_of_characters,
                               limit=limit,
                               page=0,
                               total_pages=0,
                               skip=skip,
                                attributes=all_attributes,
                                selected_filters={})

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
                               limit=limit, skip=skip,
                               attributes=all_attributes,
                               selected_filters={})


@app.route('/characters/search') # endoint to return a character searched by Id
def search_by_id():
    id = request.args.get("search")
    character_searched = storage.search_character_by_id(int(id)) # Using the function from Storage to get the character
    if character_searched == None:
        return "No Character found"
    return render_template('search.html', character=character_searched)

@app.route('/characters/filters') # endpoint to return the filtered characters
def filters():
    attributes = storage.get_attributes_dictionary()
    age_more_than = request.args.get("age_more_than", default=None, type=int)
    age_less_than = request.args.get("age_less_than", default=None, type=int)
    sort_by = request.args.get("sort_by")
    order = request.args.get("order")
    list_of_characters = storage.get_characters()


    selected_filters = {}
    for title in attributes:
        selected_values = request.args.getlist(title.lower())
        if selected_values:
            selected_filters[title.lower()] = selected_values

    sorted_characters = sorting_by(list_of_characters, sort_by, order)

    filtered_characters = filter_char(sorted_characters, selected_filters)




    if len(filtered_characters) == 0:
        filtered_characters = sorted_characters # if no filter is selected, returns the complete list of characters

    #  Logic to apply the range of ages as a filter
    if age_less_than == None and age_more_than == None:
        return render_template('filters.html', characters=filtered_characters)
    else:
        for char in filtered_characters:
            if char["age"] == None:
                filtered_characters.remove(char)
        new_filtered_char = []
        if age_less_than == None:
            for char in filtered_characters:
                if char["age"] >= age_more_than:
                    new_filtered_char.append(char) 
        elif age_more_than == None:
            for char in filtered_characters:
                if char["age"] <= age_less_than:
                    new_filtered_char.append(char)
        else:
            for char in filtered_characters:
                if char["age"] <= age_less_than and int(char["age"]) >= age_more_than:
                    new_filtered_char.append(char)
        if len(new_filtered_char) == 0:
            return "No results"
        return render_template('filters.html', characters=new_filtered_char)

@app.route('/characters/add_character', methods=['GET', 'POST']) # endpoint to add a new character to the list
def add_character():
    if request.method == 'POST':
        storage.add_character(request.form['name'],
                              request.form['house'],
                              request.form['animal'],
                              request.form['symbol'],
                              request.form['nickname'],
                              request.form['role'],
                              request.form['age'],
                              request.form['death'],
                              request.form['strength']
                            )
        return redirect(url_for('home'))
    return render_template('add_character.html')

@app.route('/characters/edit_character/<int:id>', methods=["GET", "POST"])
def edit_character(id):
    list_characters = storage.get_characters()
    selected_character = {}
    for char in list_characters:
        if int(char.get("id")) == id:
            selected_character = char
            break
    if request.method == "POST":
        name = request.form['name']
        print(name)
        storage.edit_character(id,
                              request.form['name'],
                              request.form['house'],
                              request.form['animal'],
                              request.form['symbol'],
                              request.form['nickname'],
                              request.form['role'],
                              request.form['age'],
                              request.form['death'],
                              request.form['strength'])            
        return redirect(url_for('home'))
    return render_template('edit_character.html', character=selected_character)
        
        
            


        
        


    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
