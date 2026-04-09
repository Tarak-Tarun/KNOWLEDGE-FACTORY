import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
def get_connection():
    conn=psycopg2.connect(
os.getenv("connection_string")
    )
    return conn
conn=get_connection()
if conn:
    print("Connection successful")
else:
    print("Connection failed")
