from inserter import DBInserter
from selecter import DBSelecter
from dbinit import DBInit
import json

init = DBInit('localhost', 'test_db', 'root', 'root')
inserter = DBInserter('localhost', 'test_db', 'root', 'root')
selecter = DBSelecter('localhost', 'test_db', 'root', 'root')

print(selecter.select_top_5_of_rooms_with_max_diff_of_age())