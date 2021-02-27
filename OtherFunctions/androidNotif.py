from notify_run import Notify
notify=Notify()
def buyNow():
  notify.send("Buy now")
def buy(title,price,link):
  notify.send("{} at {} on {}".format(title,price,link))
