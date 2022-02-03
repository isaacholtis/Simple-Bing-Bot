import webbrowser
import random

searchNum = int(input("Please input the number of tabs you want to open.\nPlease note that the more tabs you open the more ram you will use, and we are not responsible for your computer crashing.\n-->"))
timesNum = int(input("Please input the number of times you would like to run this.\nie your inputed amount of tabs, times whatever number you input now. The max number of times is 4.\n-->"))

num = 0
webLink = []
for i in range(searchNum):
    webLink.append(f"https://www.bing.com/search?q={(i + 1)}")
for i in range(searchNum):
    webbrowser.open (webLink[i])

if timesNum == 0:
    for i in range(searchNum):
        webLink.append(f"https://www.bing.com/search?q={(i)}")
    for i in range(searchNum):
        webbrowser.open (webLink[i])

elif timesNum == 1:
    for i in range(searchNum + 1):
        webLink.append(f"https://www.bing.com/search?q={(i + 2)}")
    for i in range(searchNum + 1):
        webbrowser.open (webLink[i])

elif timesNum == 2:
    for i in range(searchNum + 2):
        webLink.append(f"https://www.bing.com/search?q={(i + 3)}")
    for i in range(searchNum + 2):
        webbrowser.open (webLink[i])

elif timesNum == 3:
    for i in range(searchNum + 3):
        webLink.append(f"https://www.bing.com/search?q={(i + 4)}")
    for i in range(searchNum + 3):
        webbrowser.open (webLink[i])

elif timesNum == 4:
    for i in range(searchNum + 4):
        webLink.append(f"https://www.bing.com/search?q={(i + 5)}")
    for i in range(searchNum + 4):
        webbrowser.open (webLink[i])

else:
    print("You either didn't input the correct number, or a number at all.")