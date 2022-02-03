import webbrowser
import random

searchNum = int(input("Please input the number of tabs you want to open.\nPlease note that the more tabs you open the more ram you will use, and we are not responsible for your computer crashing.\n-->"))


num = 0
webLink = []
for i in range(searchNum):
    webLink.append(f"https://www.bing.com/search?q={(i + 1)}")
for i in range(searchNum):
    webbrowser.open (webLink[i])
print(webLink)
