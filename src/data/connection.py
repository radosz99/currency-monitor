import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute('pragma encoding')
    except Error as e:
        print(e)

    return conn

def create_table(conn):

    create_table_sql = """ CREATE TABLE IF NOT EXISTS currency (
                                        name TEXT NOT NULL PRIMARY KEY,
                                        last_value REAL NOT NULL
                                    ); """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

    create_table_sql = """ CREATE TABLE IF NOT EXISTS currency_history (
                                        currency_id TEXT NOT NULL,
                                        raport_id INTEGER NOT NULL,
                                        value REAL NOT NULL,
                                        FOREIGN KEY(currency_id) REFERENCES currency(name),
                                        FOREIGN KEY(raport_id) REFERENCES raport(id)
                                    ); """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)   


    create_table_sql = """ CREATE TABLE IF NOT EXISTS raport (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        day TEXT NOT NULL,
                                        hour TEXT NOT NULL
                                    ); """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)   

def get_connection():
    #database = r"resources\currency_history.db"
    database = r"C:\Users\Radek\Desktop\6semestr\DPP\lab_10_selenium\e-science\resources\currency_history.db"
    #database = r"resources\currency_history.db"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        create_table(conn)
        return conn

        