import webbrowser
from random import randint
import pyautogui
import time

searchNum = int(input("Please input the number of tabs you want to open.\nEach tab will open once, and then close, so feel free to do as many as you want!\n-->"))
timeNum = int(input("Please input how long you'd like to wait between searches.\nToo short of a time may cause the page to fail to load.\n-->"))

# We want to have searchNum = the number of tabs open in the browser, and we want to create a random number to update those tabs every 15 seconds, instead of opening a new tab and using too much ram.
for i in range(searchNum):
    webbrowser.open(f"https://www.bing.com/search?q={randint(1,200)}")
    time.sleep(timeNum)
    pyautogui.hotkey('ctrl', 'w')
'''webbrowser.open("google.com")
time.sleep(3)
pyautogui.hotkey('ctrl', 'w')
print("tab closed")'''