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
    
    if save_format.lower() == 'json':
        saver = JSONSaver()
    elif save_format.lower() == 'xml':
        saver = XMLSaver()
    else:
        raise Exception('Non read format')

    inserter.insert_into_rooms_values(JSONLoader()(path_of_rooms_file))
    inserter.insert_into_students_values(JSONLoader()(path_of_students_file))

    saver(selecter.select_list_of_rooms_with_students_count(), 'list_of_rooms_with_students_count')
    saver(selecter.select_top_5_of_rooms_with_minimal_mean_age(), 'top_5_of_rooms_with_minimal_mean_age')
    saver(selecter.select_top_5_of_rooms_with_max_diff_of_age(), 'top_5_of_rooms_with_max_diff_of_age')
    saver(selecter.select_rooms_with_balance_gender_situation(), 'rooms_with_balance_gender_situation')