
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from cryptography.fernet import Fernet
import pickle
import sys
import os
import webbrowser
import time
import random
import json

for i in range(5):
    print("which browser do you want the bot to use? (the browser needs to be installed) \n1. Google Chrome\n2. Microsoft Edge\n3. Mozilla Firefox")
    BrowserChoice = str(input("[1/2/3]--> "))
    if BrowserChoice == "1":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        break
    elif BrowserChoice == "2":
        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        break
    elif BrowserChoice == "3":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        break
    else:
        print("Invalid input! Type 1, 2, or 3")

# Email web content on the Microsoft account page
EMAILFIELD = (By.ID, "i0116")
# Password web content on the Microsoft account page
PASSWORDFIELD = (By.ID, "i0118")
# Next button content on the Microsoft account page
NEXTBUTTON = (By.ID, "idSIButton9")
# Sign in button on the bing search page
SIGNINBUTTON = (By.ID, "id_a")
print("Welcome to Bing Bot! We need to do some setup, and then we'll be ready.")

for i in range(5):
    try:
        searchNum = int(input("Please input the number of searches you want completed.\nEach search will open a tab once, and then close that tab, so feel free to do as many as you want!\n-->"))
    except ValueError:
        print("You didn't input a number!\n\nTry again!\n")
        continue
    else:
        break
else:
    print("You did something wrong too many times. Try rerunning the program. :(")
    print("FATAL: unknown error")
    print("System will exit in 3 seconds")
    time.sleep(3)
    sys.exit()
# Get a variable to tell the system how long to wait before closing a tab.
for i in range(5):
    try:
        timeNum = int(input("Please input how long you'd like to wait between searches.\nToo short of a time may cause the page to fail to load.\nWe reccomend about 5 seconds per search as that produces good results and registers searches.\n-->"))
    except ValueError:
        print("You didn't input a number!\n\nTry agian!\n")
        continue
    else:
        break
else:
    print("You did something wrong too many times. Try rerunning the program. :(")
    print("FATAL: unknown error")
    print("System will exit in 3 seconds")
    time.sleep(3)
    sys.exit()

# get username and see if user exists in the json file (database)
makeaccount = ''
username = input("What is your username? enter in any username you want if this is your first time with the bot or you want to create new credentials for the microsoft account to use\n--> ")
database = open('info.json', 'r')
database2 = json.load(database)
if username == database2['username']:
    email = database2['email']
    decryptkey = Fernet(bytes(database2['enckey'], 'utf-8'))
    password = decryptkey.decrypt(bytes(database2['encpassword'], 'utf-8'))

# if the username doesnt match, the program asks the user to make a new profile

elif username != database2['username']:
    for i in range(5):
        makeaccount = str(input("you're username doesn't exist in the bot's database.\nwould you like to make a new one? [Y/n]--> "))
        if makeaccount.lower() == "y" or makeaccount.lower() == "n":
            break
        else:
            print("Invalid input. Type y or n.")

    if makeaccount.lower() == "y":
        newusername = input("Type the username that you want to use for this bot.\n--> ")
        newemail = input("Type the email address that you use for your microsoft account.\n--> ")
        insecurenewpassword = bytes(input("Type the password for your microsoft account.(it will be encrypted)\n--> "), 'utf-8')
        newenckey = Fernet.generate_key()
        f = Fernet(newenckey)
        newencpassword = f.encrypt(insecurenewpassword)
database.close()
if makeaccount.lower() == "y":
    with open('info.json', 'w') as savefile:
        infodict = {'email': str(newemail), 'encpassword': str(newencpassword, 'utf-8'), 'enckey': str(newenckey, 'utf-8'), 'username': str(newusername)}
        jsonobject = json.dumps(infodict)
        savefile.write(jsonobject)
    infofile = open('info.json', 'r')
    infofile2 = json.load(infofile)
    email = infofile2['email']
    decryptkey = Fernet(bytes(infofile2['enckey'], 'utf-8'))
    password = decryptkey.decrypt(bytes(infofile2['encpassword'], 'utf-8'))
    print(password)
    infofile.close()

print("Okay! Starting login, and searches!")

# Defines the funtion that the threads use later on to search...
# t1 represents which WebDriver that thread uses, the first or the second one...
# You need to WebDrivers because you can't control more than one tab at a time...
# I think we should make a for loop that desides how many WebDriver instances you would have...
# but that would be burdensome to implement

#don't change these lists, except for adding more verbs to verblist
#formula for how many possible searches: multiply the len of each list by each other (except searchlist)
startlist = ['why', 'how', 'what', 'where', 'when', 'who',]
auxlist = ['do', 'is', 'did', 'will', 'has', 'does']
subjectlist = ['you', 'i', 'we']
verblist = ['study', 'like', 'do', 'love', 'change', 'find', 'create', 'build']

#add any nouns you want to infolist; it gives the bot more content to work with
infolist = ['dogs', 'microsoft', 'cars', 'food', 'walmart', 'grammarly', 'california', 'debate', 'monitor', 'paper', 'marvel', 'dc', 'tesla', 'dream', 'python', 'github', 'ram', 'ford', 'strike', 'amazon', 'aws']

#searchlist is a list of all of the completed searches, used to make sure the bot doesnt repeat the same search over again.
searchlist = []

def searchNumR(n1, n2):
    for i in range(n1):
        while True:
            searchterm = f'https://www.bing.com/search?q={random.choice(startlist)}+{random.choice(auxlist)}+{random.choice(subjectlist)}+{random.choice(verblist)}+{random.choice(infolist)}'
            if searchterm not in searchlist:
                searchlist.append(searchterm)
                break
        try:
            driver.get(searchterm)
            time.sleep(n2)
        except:
            time.sleep(n2)
            if i + 1 == 1:
                serNum = "1st"
            else:
                serNum = f"{i + 1}d"
            print(f"Hmm, the {serNum} search didn't work. do you have internet? Trying again.")
            continue
for i in range(5):
    try:
        # Login for the first webdriver instance
        driver.get('https://login.live.com')
        # Wait for email field and enter email
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
        # Click Next
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        # Wait for password field and enter password
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(str((password), 'utf-8'))
        # Click Login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        # Click Yes
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        time.sleep(5)
        break
    except:
        print("Login failed. trying again.")
        continue
else:
    print("The login won't work. make sure you entered in the correct email and password for your account when you set up the bot")
    print("We'll run the searches, but you might not get points for them. press CTRL + C or COMMAND + C to cancel.")
time.sleep(3)

#function to run the searches
searchNumR(searchNum, timeNum)

#wait 3 seconds and then close the program
time.sleep(3)
driver.close()
print("Searches completed succsesfully! Thanks for using our bot!")
