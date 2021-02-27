# used to get the data from webpages when url is provided
import requests

# used to delay the code
from time import sleep

# Used to parse data provided by requests to extract the data required
from bs4 import BeautifulSoup


class AmazonTracker:
    pass


# after the code runs once a break of 20 seconds is given before running again
while KeyboardInterrupt:

    print('All products have been checked\n')
    print('Enter ctrl + c to exit code')

    sleep(20)  # Stops the code process for 20 seconds
