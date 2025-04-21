from data_manager.config import config
from data_manager.storage_postgres import PostgreStorage


params = config()

storage = PostgreStorage(params)
#add_character(self, name, house, animal, symbol, nickname, role, age, death, strength)
print(storage.get_characters())
#storage.delete_character(id=52)