import psycopg2 #type: ignore
from dotenv import load_dotenv #type: ignore
import os
import json
import logging
from datetime import datetime

logging.basicConfig(filename="task_manager.log", level=logging.INFO)



load_dotenv()

def get_connection():
    try:
        return psycopg2.connect(os.getenv("DATABASE_URL"))
    except:
        return None

class Task:
    def __init__(self, title, description, status="pending", created_at=None):
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.now()

class TaskManager:
    def __init__(self):
        self.conn = get_connection()

    def add_task(self, task):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tasks (title, description, status, created_at) VALUES (%s,%s,%s,%s)",
                    (task.title, task.description, task.status, task.created_at))
        self.conn.commit()

    def list_tasks(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks")
        for row in cur.fetchall():
            print(row)

    def complete_task(self, tid):
        cur = self.conn.cursor()
        cur.execute("UPDATE tasks SET status='completed' WHERE id=%s", (tid,))
        self.conn.commit()

    def delete_task(self, tid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id=%s", (tid,))
        self.conn.commit()

    def search(self, key):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE title ILIKE %s OR description ILIKE %s",
                    (f"%{key}%", f"%{key}%"))
        for row in cur.fetchall():
            print(row)

    def filter(self, status):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE status=%s", (status,))
        for row in cur.fetchall():
            print(row)

    def export_json(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM tasks")
        data = [{"id":r[0],"title":r[1],"desc":r[2],"status":r[3],"created":str(r[4])} for r in cur.fetchall()]
        with open("tasks.json","w") as f:
            json.dump(data,f,indent=2)

def main():
    tm = TaskManager()
    while True:
        print("\n1 Add 2 List 3 Complete 4 Delete 5 Search 6 Filter 7 Export 8 Exit")
        c = input("Choice: ")
        try:
            if c=="1":
                t = input("Title: ")
                d = input("Desc: ")
                tm.add_task(Task(t,d))
            elif c=="2":
                tm.list_tasks()
            elif c=="3":
                tm.complete_task(int(input("ID: ")))
            elif c=="4":
                tm.delete_task(int(input("ID: ")))
            elif c=="5":
                tm.search(input("Keyword: "))
            elif c=="6":
                tm.filter(input("Status: "))
            elif c=="7":
                tm.export_json()
            elif c=="8":
                break
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    main()