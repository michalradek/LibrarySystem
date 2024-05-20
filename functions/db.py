import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv("db_creds.env")


class Sql_Database:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Sql_Database, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
        return cls._instance

    def fetch_one(self, que, params=None):
        cursor = self.connection.cursor(buffered=True)
        if params:
            cursor.execute(que, params)
        else:
            cursor.execute(que)
        res = cursor.fetchone()
        cursor.close()
        return res

    def fetch_all(self, que, params=None):
        cursor = self.connection.cursor(buffered=True)
        if params:
            cursor.execute(que, params)
        else:
            cursor.execute(que)
        res = cursor.fetchall()
        cursor.close()
        return res

    def exe(self, query, params=None):
        cursor = self.connection.cursor(buffered=True)
        try:
            if params:
                cursor.execute(query,params)
            else:
                cursor.execute(query)
        except ValueError:
            print(ValueError)
        self.connection.commit()
        cursor.close()
