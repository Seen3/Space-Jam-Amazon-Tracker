# used to get the data from webpages when url is provided
import requests

# used to delay the code
from time import sleep

# Used to parse data provided by requests to extract the data required
from bs4 import BeautifulSoup

# miscellaneous functions that are repeated but simple
from OtherFunctions.MiscFunctions import *

# Import the sql functions that access database
from OtherFunctions.SQL_Functions import Database

from OtherFunctions.Send_Email import send_mail


class AmazonTracker:
    # Constructor of the class it checks if the database file exists, and if it doesn't it creates one
    # and asks for user details and product urls
    def __init__(self):
        params = db.access_product_params()
        for param in params:
            self.url = param[0]
            self.maxPrice = int(param[1])
            self.connect()
            self.extract_data()

    # connects to the webpage provided using the url
    def connect(self):
        print("\n\nPlease wait. We are attempting to connect to the product page")

        # The headers are used to make the code imitate a browser and prevent amazon from block it access to the site.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip',
            'DNT': '1',  # Do Not Track Request Header
            'Connection': 'close'
        }

        # Get the code of the product page using the url provided
        self.response = requests.get(self.url, headers=headers)

        # code proceeds only if the connection to the product page is successful
        if self.response:
            print("Connected successfully\nProcessing data. Please wait\n\n")
        else:
            print("Connection failed")
            exit()


# after the code runs once a break of 20 seconds is given before running again
while KeyboardInterrupt:
    db = Database()
    AmazonTracker()

    print('All products have been checked\n')
    print('Enter ctrl + c to exit code')

    sleep(20)  # Stops the code process for 20 seconds
