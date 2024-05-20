from functions.db import Sql_Database
from dotenv import load_dotenv

load_dotenv("functions/db_creds.env")
db = Sql_Database()


def print_all(callback):
    query = "SELECT * FROM books;"
    rows = db.fetch_all(query)
    print()
    for row in rows:
        print("ID: "+str(row[0]))
        print("Title: "+row[1])
        print("Author: "+row[2])
        print("Quantity: "+str(row[3]))
        for x in range(15):
            print("-", end=" ")
        print()
    input("\nPress any key to continue.")
    callback()


def add_book(callback):
    params = None
    try:
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        quantity = int(input("Enter the quantity: "))
        params = (title, author, quantity)
        query = 'INSERT INTO books(title, author, quantity) VALUES (%s,%s,%s);'
        db.exe(query, params)
    except ValueError:
        input("Enter correct data. Press any key to continue")
    callback()
