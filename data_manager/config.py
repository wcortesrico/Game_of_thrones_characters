from configparser import ConfigParser
import os

# Parsing configuration data for PostgreSQL database
def config(filename="database.ini", section="postgresql"):
    #create parser
    parser = ConfigParser()
    
    # Construct the absolut path to database.ini in the same directory
    filepath = os.path.join(os.path.dirname(__file__), filename)

    #read config file
    parser.read(filepath)
    db ={}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section{0} is not found in {1} file.". format(section, filename))
    
    return db
