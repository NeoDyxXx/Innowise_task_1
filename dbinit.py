import psycopg2
import time

class DBInit:
    def __init__(self, host: str, db_name: str, user: str, password: str) -> None:
        self.__host = host
        self.__db_name = db_name
        self.__user = user
        self.__password = password

        self.__init_connect()
        self.__init_tables()

    def __init_connect(self):
        while True:
            try:
                self.conn = psycopg2.connect(dbname=self.__db_name, user=self.__user,\
                                password=self.__password, host=self.__host)
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