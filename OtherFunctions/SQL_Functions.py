# used to check if a given file exists or not
import os.path

# used to create, modify and store database files using sql
import sqlite3 as sql

# miscellaneous functions that are repeated but simple
from OtherFunctions.MiscFunctions import *


class Database:
    def __init__(self):
        # If the file does not exist then create one and ask user for email and check frequency
        if not self.file_exists():
            self.connect()
            self.create_tables()

        else:
            self.connect()

    '''
        These functions will get data from user and store it in the database
    '''

    # Checks if a given file exists
    @staticmethod
    def file_exists():
        if os.path.isfile('OtherFunctions/Database.db'):
            return True
        else:
            return False

    # Attempts connection to the database file
    def connect(self):
        try:
            self.con = sql.connect('OtherFunctions/Database.db')
        except sql.Error:
            print(sql.Error)
            exit()

        # Create a cursor using the connection to the database
        self.c = self.con.cursor()

    # Create tables url and user for first time initialization
    def create_tables(self):
        self.c.execute('CREATE TABLE URL(url, maxPrice, availabilityAlertEmail, availabilityAlertNotification)')
        self.c.execute('CREATE TABLE USER(username, email, checkFrequency)')