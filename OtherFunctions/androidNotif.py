from notify_run import Notify
notify=Notify()
def buyNow():
  notify.send("Buy now")
def buy(title,price,link):
  notify.send("""
The price of the product "{}" has gone below the threshold you have entered to the price Rs.{}.
Here is the link {}
""".format(title,price,link))
