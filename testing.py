from storage_json import Storage

storage = Storage("characters.json")

all_characters = storage.get_characters()
all_attributes = storage.get_all_attributes()
all_titles = storage.get_all_attributes_title()


storage.edit_character(51, "Walter", "Ndfv", "fdfv", "w", "e", "e", 31, 39, "er")

