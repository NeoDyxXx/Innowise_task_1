from dbinit import DBInit

class DBInserter(DBInit):
    def __init__(self, host: str, db_name: str, user: str, password: str) -> None:
        super().__init__(host, db_name, user, password)

    def insert_into_rooms_value(self, id: int, name: str):
        with self.conn.cursor() as cursor:
            cursor.execute('''insert into rooms values ({0}, '{1}')'''.format(id, name))
            self.conn.commit()

    def insert_into_rooms_values(self, list_values: dict):
        with self.conn.cursor() as cursor:
            for item in list_values:
                try:
                    cursor.execute('''insert into rooms values ({0}, '{1}')'''.format(item['id'], item['name']))
                except:
                    pass
            self.conn.commit()

    def insert_into_students_value(self, id: int, name: str, room: int, sex: str, birthday: str):
        with self.conn.cursor() as cursor:
            cursor.execute('''insert into students values ({0}, '{1}', {2}, '{3}', to_date('{4}', 'YYYY-MM-DDTHH24:MI:SS.US'))'''.format(id, name, room, sex, birthday))

    def insert_into_students_values(self, list_values: dict):
        with self.conn.cursor() as cursor:
            for item in list_values:
                try:
                    cursor.execute('''insert into students values ({0}, '{1}', {2}, '{3}', to_date('{4}', 'YYYY-MM-DDTHH24:MI:SS.US'))'''
                        .format(item['id'], item['name'], item['room'], item['sex'], item['birthday']))
                except:
                    pass
            self.conn.commit()