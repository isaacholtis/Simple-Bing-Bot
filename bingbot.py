import webbrowser
from random import randint
import pyautogui
import time
import threading

# Define webOpenSearch, which is used for threading so that multiple tabs can be opened at once.
def webOpenSearch(n, n2):
    for i in range(n):
        webbrowser.open(f"https://www.bing.com/search?q={randint(1,2000)}")
        time.sleep(n2)
        pyautogui.hotkey('ctrl', 'w')
# Get a variable to tell the system how many tabs to open.
searchNum = int(input("Please input the number of tabs you want to open.\nEach tab will open once, and then close, so feel free to do as many as you want!\n-->"))
# Get a variable to tell the system how long to wait before closing a tab.
# Note that I can't get the tabs to close well, with the system usually only closing one or two tabs.
timeNum = int(input("Please input how long you'd like to wait between searches.\nToo short of a time may cause the page to fail to load.\n-->"))

# Opens a web page to keep the browser window open, for lighter resource usage, and faster operation.
webbrowser.open("Dep1Browser.html")
time.sleep(3)
# Create a for loop that makes the threads needed to have multiple tabs open, using searchNum to detirmine how many there are.
for i in range(searchNum):
    i = threading.Thread(target=webOpenSearch, args=(searchNum,timeNum))
    i.start()
