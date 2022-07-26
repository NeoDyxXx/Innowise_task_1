from pip import main
from inserter import DBInserter
from selecter import DBSelecter
from saver_json import JSONSaver
from loader_json import JSONLoader
from saver_xml import XMLSaver
import os


if __name__ == '__main__':
    host = os.environ.get('host', 'localhost')
    db_name = os.environ.get('db_name', 'test_db')
    user_name = os.environ.get('user_name', 'root')
    password = os.environ.get('password', 'root')

    path_of_students_file = os.environ.get('students', 'data/students.json')
    path_of_rooms_file = os.environ.get('rooms', 'data/rooms.json')
    save_format = os.environ.get('save_format', 'json')

    inserter = DBInserter(host, db_name, user_name, password)
    selecter = DBSelecter(host, db_name, user_name, password)
    
    print(selecter.select_top_5_of_rooms_with_minimal_mean_age())