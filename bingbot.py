from random import randint
import time
import threading
from selenium import webdriver

whatBrowse = webdriver.Edge()
whatBrowse2 = webdriver.Edge()
# Get a variable to tell the system how many tabs to open.
searchNum = int(input("Please input the number of searches you want completed.\nEach search will open a tab once, and then close that tab, so feel free to do as many as you want!\n-->"))
# Get a variable to tell the system how long to wait before closing a tab.
timeNum = int(input("Please input how long you'd like to wait between searches.\nToo short of a time may cause the page to fail to load.\n-->"))
tabNum = int(input("Please input how many tabs you'd like open at once.\n-->"))
def searchNumR(n1,n2, t1):
    for i in range(n1):
        t1.get(f"https://www.bing.com/search?q={randint(1,2000)}")
        time.sleep(n2)
        print("This thread is running fine, and the tab was closed.")

# For loops to create two instances running at once.
for i in range(tabNum):
    i = threading.Thread(target=searchNumR, args=(searchNum,timeNum,whatBrowse))
    i.start()
for i in range(tabNum):
    i = threading.Thread(target=searchNumR, args=(searchNum,timeNum,whatBrowse2))
    i.start()