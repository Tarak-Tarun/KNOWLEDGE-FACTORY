import psycopg2
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

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
        image_url TEXT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created successfully")
    cursor.close()
    conn.close()
def insert_data(name,email,password,img_url):
    conn=get_connection()
    cursor=conn.cursor()
    insert_query="""
    INSERT INTO users(name,email,password,image_url) VALUES(%s,%s,%s,%s);
    """
    cursor.execute(insert_query,(name,email,password,img_url))
    conn.commit()
    if cursor.rowcount>0:
        print("Data inserted successfully")
    cursor.close()
    conn.close()
if __name__=="__main__":
    name=input("Enter name:")
    email=input("Enter email:")
    password=input("Enter password:")
    img_url=input("Enter image url:")
    password_hash=generate_password_hash(password)
    insert_data(name, email, password_hash, img_url)
