from OtherFunctions.SQL_Functions import Database

from Amazon_Tracker import AmazonTracker

# This tells the constructor to disable alerts
AT = AmazonTracker(alert_confirmation=False, loop=False)

option = input('1: List all the products\n'
               '2: Add products\n'
               '3: Remove products\n')

if option == '1':
    AT.extract_data()
elif option == '2':
    db = Database()
    db.get_product_params()
elif option == '3':
    print('This feature is in development')
