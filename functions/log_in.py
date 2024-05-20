from functions.db import Sql_Database
from dotenv import load_dotenv
from hashlib import sha256
import getpass


load_dotenv("functions/db_creds.env")
db = Sql_Database()


def log_in():
    username = input("Enter your username: ")
    password = sha256(getpass.getpass("Enter your password: ").encode('utf-8')).hexdigest()
    params = (username, password)
    query = 'SELECT COUNT(ID) FROM accounts WHERE username = %s AND password = %s;'
    row = db.fetch_one(query, params)
    if row[0] == 1:
        return True
    else:
        return False
