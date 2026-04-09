import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
def get_connection():
    conn=psycopg2.connect(
os.getenv("connection_string")
    )
    return conn
def Table_create():
    conn=get_connection()
    cursor=conn.cursor()
    create_table_query="""
    CREATE TABLE IF NOT EXISTS users(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        PASSWORD TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created successfully")
    cursor.close()
    conn.close()
if __name__=="__main__":

    Table_create()