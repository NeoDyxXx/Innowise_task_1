import psycopg2
import time

class DBInit:
    def __init__(self, host: str, db_name: str, user: str, password: str) -> None:
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password

        self.__init_connect()
        self.__init_tables()

    def insert_into_rooms_value(self, id: int, name: str):
        with self.conn.cursor() as cursor:
            cursor.execute('''insert into rooms values ({0}, '{1}')'''.format(id, name))
            self.conn.commit()

    def insert_into_rooms_values(self, list_values: dict):
        with self.conn.cursor() as cursor:
            for item in list_values:
                cursor.execute('''insert into rooms values ({0}, '{1}')'''.format(item['id'], item['name']))
            self.conn.commit()

    def insert_into_students_value(self, id: int, name: str, room: int, sex: str, birthday: str):
        with self.conn.cursor() as cursor:
            cursor.execute('''insert into students values ({0}, '{1}', {2}, '{3}', to_date('{4}', 'YYYY-MM-DDTHH24:MI:SS.US'))'''.format(id, name, room, sex, birthday))

    def insert_into_students_values(self, list_values: dict):
        with self.conn.cursor() as cursor:
            for item in list_values:
                cursor.execute('''insert into students values ({0}, '{1}', {2}, '{3}', to_date('{4}', 'YYYY-MM-DDTHH24:MI:SS.US'))'''
                    .format(item['id'], item['name'], item['room'], item['sex'], item['birthday']))
            self.conn.commit()

    def select_data_of_rooms(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select * from rooms')
            return cursor.fetchall()
    
    def select_data_of_students(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select * from students')
            return cursor.fetchall()

    def __init_connect(self):
        while True:
            try:
                self.conn = psycopg2.connect(dbname=self.db_name, user=self.user,\
                                password=self.password, host=self.host)
                break
            except:
                print("Error from connect")
                time.sleep(1.5)

    def __init_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''create table if not exists rooms 
                                (
                                    id bigint primary key, 
                                    name varchar(50)
                                )''')
            
            cursor.execute('''create table if not exists students 
                                (
                                    id bigint primary key,
                                    name varchar(50),
                                    room bigint ,
                                    sex varchar(1),
                                    birthday date,
                                    FOREIGN KEY (room) REFERENCES rooms (id)
                                )''')
            self.conn.commit()

    def __drop_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute('drop table if exists students')
            cursor.execute('drop table if exists rooms')
            self.conn.commit()