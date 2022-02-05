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
def searchNumR(n1,n2):
    for i in range(n1):
        whatBrowse.execute_script(f"window.open('https://www.bing.com/search?q={randint(1,2000)}','newTab{i}');")
        whatBrowse.switch_to.window(f"newTab{i}")
        whatBrowse.get(f"https://www.bing.com/search?q={randint(1,2000)}")
        time.sleep(n2)
        whatBrowse.close()
        print("This thread is running fine, and the tab was closed.")
def searchNumR2(n1,n2):
    for i in range(n1):
        whatBrowse2.execute_script(f"window.open('https://www.bing.com/search?q={randint(1,2000)}','newTab{i}');")
        whatBrowse2.switch_to.window(f"newTab{i}")
        whatBrowse2.get(f"https://www.bing.com/search?q={randint(1,2000)}")
        time.sleep(n2)
        whatBrowse2.close()
        print("This thread is running fine, and the tab was closed.")
def tabFunc(n):
    for i in range(n):
        i = threading.Thread(target=searchNumR, args=(searchNum,timeNum))
        i.start()
def tabFunc2(n):
    for i in range(n):
        i = threading.Thread(target=searchNumR2, args=(searchNum,timeNum))
        i.start()

# Using threads so they both run at the same time.
t1 = threading.Thread(target=tabFunc, args=(tabNum / 2))
t2 = threading.Thread(target=tabFunc2, args=(tabNum / 2))