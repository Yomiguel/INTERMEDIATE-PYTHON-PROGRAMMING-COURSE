#from python to JSON (Serialization, Encode)// dictionary in python is a object in JSON.
import json
from json.encoder import JSONEncoder

users = {
    'name' : 'Luis',
    'age': 30,
    'city': 'Cali',
    'hasChildren': False,
    'id' : 1234,
    'profession' : ['Engineer, Programmer']
}

users_JSON = json.dumps(users, indent = 4, sort_keys = True)
#print(users_JSON)

#Convert Python objects into JSON objects and save them into a file with the json.dump() method.
with open('users.json', 'w') as file:
    json.dump(users, file, indent = 4, sort_keys = True)

#From JSON to Python (Deserialization, Decode)
#Convert a JSON string into a Python object with the json.loads() method. The result will be a Python dictionary.

users2 = json.loads(users_JSON)
print(users2)

#Load data from a file and convert it to a Python object with the json.load() method.
with open('users.json', 'r') as file2:
    users2a = json.load(file2)
print(users2a) 