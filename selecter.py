from dbinit import DBInit

class DBSelecter(DBInit):
    def __init__(self, host: str, db_name: str, user: str, password: str) -> None:
        super().__init__(host, db_name, user, password)

    def select_data_of_rooms(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select * from rooms')
            return cursor.fetchall()
    
    def select_data_of_students(self):
        with self.conn.cursor() as cursor:
            cursor.execute('select * from students')
            return cursor.fetchall()

    def select_list_of_rooms_with_students_count(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''select rooms.name, count(*) from rooms inner join students 
                              on rooms.id = students.room
                              group by rooms.name''')
            return cursor.fetchall()

    def select_top_5_of_rooms_with_minimal_mean_age(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''select rooms.id, rooms.name
                              from rooms inner join students 
                              on rooms.id = students.room
                              group by rooms.id
                              order by avg(current_date::timestamp - students.birthday::timestamp) asc''')
            return cursor.fetchall()[:5]

    def select_top_5_of_rooms_with_max_diff_of_age(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''select rooms.id, rooms.name
                              from rooms inner join students 
                              on rooms.id = students.room
                              group by rooms.id
                              order by max(current_date::timestamp - students.birthday::timestamp) - min(current_date::timestamp - students.birthday::timestamp) desc''')
            return cursor.fetchall()[:5]

    def select_rooms_with_balance_gender_situation(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''select distinct r1.id, r1.name from rooms as r1
                              where exists(select * from rooms as r2 inner join students as s2
                                           on r2.id = s2.room where r1.id = r2.id and s2.sex = 'M') and
                                    exists(select * from rooms as r2 inner join students as s2
                                           on r2.id = s2.room where r1.id = r2.id and s2.sex = 'F')
                              order by r1.id''')
            return cursor.fetchall()