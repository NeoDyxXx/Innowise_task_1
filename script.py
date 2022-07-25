import imp
from dbinit import DBInit
import json

init = DBInit('localhost', 'test_db', 'root', 'root')

with open('data/rooms.json', 'r') as json_file:
    data = json.load(json_file)

init.insert_into_rooms_values(data)

with open('data/students.json', 'r') as json_file:
    data = json.load(json_file)

init.insert_into_students_values(data)

print(init.select_data_of_rooms())
print(init.select_data_of_students())