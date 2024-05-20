from functions.db import Sql_Database
from dotenv import load_dotenv

load_dotenv("functions/db_creds.env")
db = Sql_Database()


def print_all(callback):
    query = "SELECT * FROM books;"
    rows = db.fetch_all(query)
    for row in rows:
        print("ID: "+str(row[0]))
        print("Title: "+row[1])
        print("Author: "+row[2])
        print("Quantity: "+str(row[3]))
        for x in range(15):
            print("-", end=" ")

    input("test")
    callback()


def add_book():
    query = "INSERT INTO books (title, author, quantity) VALUES "

