import psycopg2
from datetime import datetime


class PostgresApi():
    def __init__(self):
        self.connection = psycopg2.connect(
            host = "127.0.0.1",
            user = "postgres",
            password = "password",
            database = "test_db"
        )
        self.cursor = self.connection.cursor()
        self.connection.autocommit = True

    def create_table(self):
        try:
            # create_table = ''' CREATE TABLE test_table
            #     (Id serial PRIMARY KEY,
            #     Text text NOT NULL,
            #     Date timestamp
            #     )
            #     '''
            create_table = ''' CREATE TABLE IF NOT EXISTS test_table
                (Id serial PRIMARY KEY,
                Text text NOT NULL,
                Date timestamp
                )
                '''
            self.cursor.execute(create_table)


        except Exception as _ex:
            print("[INFO] Error whith PostgrSQL: ", _ex)

    def put_data(self, data):

        try:
            dt = datetime.now()
            add_data = f''' INSERT INTO test_table (Text, Date) VALUES('{data}', '{dt}'); '''
            self.cursor.execute(add_data)

        except Exception as _ex:
            print("[INFO] Error whith PostgrSQL: ", _ex)

    def table_exist(self):
        self.cursor.execute('''SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME='test_table';''')
        return bool(self.cursor.rowcount)

    def get_data(self, id):
        self.cursor.execute('''SELECT * FROM "test_table"''')
        for row in self.cursor:
            if row[0] == id:
                print(row)
                return(row)

    def list_data(self):
        self.cursor.execute('''SELECT * FROM "test_table"''')
        list= {}
        for row in self.cursor:
            list[row[0]] = str(row[2])
        return list

con = PostgresApi()
con.create_table()
con.put_data("hello")
print(con.table_exist())
con.get_data(1)
con.list_data())


