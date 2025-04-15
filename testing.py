from storage_json import Storage

storage = Storage("characters.json")

all_characters = storage.get_characters()
all_attributes = storage.get_all_attributes()
all_titles = storage.get_all_attributes_title()

def sort_by(char_list, sort_by, order):
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
    

sort_by(all_characters, "house", "sort_asc")