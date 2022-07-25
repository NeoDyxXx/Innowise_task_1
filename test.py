import psycopg2
conn = psycopg2.connect(dbname='test_db', user='root', 
                        password='root', host='localhost')
cursor = conn.cursor()

cursor.close()