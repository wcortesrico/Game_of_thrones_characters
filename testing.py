from storage_json import Storage

storage = Storage("characters.json")

all_characters = storage.get_characters()
all_attributes = storage.get_all_attributes()
all_titles = storage.get_all_attributes_title()

"""""

attributes = {}
# attributes["name"] = 

for title in all_titles:
    temp = []
    for character in all_characters:
        for attribute in all_attributes:
            if character[title] == attribute and attribute not in temp:
                temp.append(attribute)
            attributes[title] = temp

for attribute in attributes:
    print(attribute)
    for attr in attributes[attribute]:
        print(attr)
    print("")

"""""

retrieve_dic = {
    "house": ["Targaryen", "Lannister"]
}

print(storage.filter_char(retrieve_dic))