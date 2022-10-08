import psycopg2
from datetime import datetime
from config import host, user, password, db_name
dt = datetime.now()

try:
    #connect to exist db
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    cursor = connection.cursor()
    create_table = ''' CREATE TABLE test_table
    (Id serial PRIMARY KEY,
    Text text NOT NULL,
    Date timestamp
    )
    '''
    cursor.execute(create_table)
    connection.commit()
    print("table created")
except Exception as _ex:
    print("[INFO] Error whith PostgrSQL: ", _ex)
#
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")

def put(data):
    try:
        #connect to exist db
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        with connection.cursor() as cursor:
            add_data = f''' INSERT INTO test_table (Text, Date) VALUES('{data}', '{dt}'); '''
            cursor.execute(add_data)
            connection.commit()

    except Exception as _ex:
        print("[INFO] Error whith PostgrSQL: ", _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")


put("some text 1")

