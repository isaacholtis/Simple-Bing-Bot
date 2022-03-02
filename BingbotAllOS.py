#!/bin/python3
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
import threading
import time
import random
import itertools

# Make a cool loading animation
# Function to create the animation
def animated_marker():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone loading!     ')

#check what search engine to use
for i in range(5):
    try:
        print("which browser do you want the bot to use? (the browser needs to be installed) \n1. Google Chrome\n2. Microsoft Edge\n3. Mozilla Firefox")
        BrowserChoice = int(input("[1/2/3]--> "))
        if BrowserChoice == 1:
            done = False
            t1 = threading.Thread(target = animated_marker)
            t1.start()
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            done = True
            break
        elif BrowserChoice == 2:
            done = False
            t1 = threading.Thread(target = animated_marker)
            t1.start()
            service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
            done = True
            break
        elif BrowserChoice == 3:
            done = False
            t1 = threading.Thread(target = animated_marker)
            t1.start()
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
            done = True
            break
    except ValueError:
        error = "User typed a string, needed an int."
        print("Invalid input! Type 1, 2, or 3")
        continue
    except:
        error = "Uknown error."
        continue
else:
    print("Fatal: " + error)
    print("System will exit in 3 seconds.")
    time.sleep(2.9)
    sys.exit()


# Email web content on the Microsoft account page
EMAILFIELD = (By.ID, "i0116")
# Password web content on the Microsoft account page
PASSWORDFIELD = (By.ID, "i0118")
# Next button content on the Microsoft account page
NEXTBUTTON = (By.ID, "idSIButton9")
# Sign in button on the bing search page
SIGNINBUTTON = (By.ID, "id_a")
print("\n\n\nWelcome to Bing Bot! We need to do some setup, and then we'll be ready.")

for i in range(5):
    try:
        # Loads the pickle files with the user dictionarys 
        with open('encEPwd.pkl', 'rb') as encOpenEmail:
            encFiles = pickle.load(encOpenEmail)
        with open('encKey.pkl', 'rb') as encOpenKey:
            encFilesKey = pickle.load(encOpenKey)
        with open('wordList.pkl', 'rb') as wordList:
            infolist = pickle.load(wordList)
        break
    except:
        encFiles = {}
        encFilesKey = {}
        infolist = ['dogs', 'microsoft', 'cars', 'food', 'walmart', 'grammarly', 'california', 'debate', 'monitor', 'paper', 'marvel', 'dc', 'tesla', 'dream', 'python', 'github', 'ram', 'ford', 'strike', 'amazon', 'aws']
        print("User info couldn't be loaded, but we are continuing anyway, with new database files.")
        break
else:
    print(f"FATAL: Uknown error")
    print("System will exit in 3 seconds")
    time.sleep(3)
    sys.exit()
# Get a variable to tell the system how many searches each thread completes...
# This will be double the searches intended by the user, so we need to fix that
time.sleep(0.5)
for i in range(5):
    try:
        searchNum = int(input("\nPlease input the number of searches you want completed.\nEach search will open a tab once, and then close that tab, so feel free to do as many as you want!\n-->"))
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

# Gets the name of the user, so we can check if they have entered their credentials before
for i in range(5):
    try:
        userName = input("We need your Microsoft account details so we can sign you in to save your search points.\nPlease input your first and last name so we can store you encrypted username and password.\nOr, if you don't want to save your details, there will be an option to opt out, and you can just enter them, but they won't be saved.\nIf you've already entered your email and password once, then put in your name, and we'll load your profile if it exists in our system.\n-->")
    except ValueError:
        print("You didn't type letters!\n\nTry again!\n")
        continue
    else:
        break
else:
    print("You did something wrong too many times. Try rerunning the program. :(")
    print("FATAL: unknown error")
    print("System will exit in 3 seconds")
    time.sleep(3)
    sys.exit()

# If the user has entered credentials, the system won't ask again
try:
    if userName + " Email" in encFiles:
        print("You exist in our system! Logging you in now!")
        emailCrypt = encFiles[userName + " Email"]
        emailKey = encFilesKey[userName + " keyEmail"]
        email = emailKey.decrypt(emailCrypt).decode()
        pwdCrypt = encFiles[userName + " Password"]
        pwdKey = encFilesKey[userName + " keyPwd"]
        pwd = pwdKey.decrypt(pwdCrypt).decode()
    # If the user has not entered credentials before, the system will ask the user to enter them
    else:
        enrollDetails = str.lower(input("Would you like us to save your account? This will erase any other users.\nType yes or no.\n-->"))
        if enrollDetails == "yes":
            for i in range(5):
                try:
                    email = input("Please enter your Microsoft account email.\n-->")
                    break
                except:
                    print("Sorry! You typed a number, but we need a letter! Try again!")
                    continue
            else:
                print("Sorry! There was an error saving your account details, so we couldn't continue!")
                print("Exiting in 3 seconds.")
                print("FATAL: unknown error")
            for i in range(5):
                try:
                    pwd = input("Please input your Microsoft account password.\n-->")
                    break
                except:
                    print("Sorry! You typed a number, but we need a letter! Try again!")
                    continue
            else:
                print("Sorry! There was an error saving your account details, so we couldn't continue!")
                print("Exiting in 3 seconds.")
                print("FATAL: unknown error")
            # Creates encryption keys, I think this could be simplified
            key = Fernet.generate_key()
            key2 = Fernet.generate_key()
            keyEmail = Fernet(key)
            keyPwd = Fernet(key2)
            # Encrypts the email and password
            encEmail = keyEmail.encrypt(email.encode())
            encPwd = keyPwd.encrypt(pwd.encode())
            # Dictionary that will be stored in a pickle file...
            # with the encrypted email and password in it with appropriate dictionary...
            #  keys to call back the email and password later
            encEPPickle = {userName + " Email": encEmail, userName + " Password": encPwd}
            try:
            # Store the dictionary in a pickle file called encEPwd.pkl
                with open('encEPwd.pkl', 'wb') as encFile:
                    pickle.dump(encEPPickle, encFile)
            except:
                print("We couldn't save your profile, but we can still continue! Would you like to? Type yes or no.\n-->")
                goOn = str.lower(input())
                if goOn == "yes":
                    pass
            # Dictionary that will be stored in a pickle file...
            #  with the decryption keys for the email and password in it with appropriate dictionary...
            #  keys to call back the decryption keys later
            encKeyPickle = {userName + " keyEmail": keyEmail, userName + " keyPwd": keyPwd}
            try:
                with open('encKey.pkl', 'wb') as encKey:
                    pickle.dump(encKeyPickle, encKey)
                print("Profile saved succesesfully!\nJust type your name next time you use the bot, and we'll remember you password.\nAnd of course, it also encrypted.")
            except:
                print("We couldn't save your profile, but we can still continue! Would you like to? Type yes or no.\n-->")
                goOn = str.lower(input())
                if goOn == "yes":
                    pass
            print("Profile saved succesesfully!\nJust type your name next time you use the bot, and we'll remember you password.\nAnd of course, it also encrypted.")
        else:
            print("Okay! We won't save your profile!")
            print("We'll still need your Microsoft account email and password to login though.")
            for i in range(5):
                try:
                    email = input("Please enter your Microsoft account email.\n-->")
                    break
                except:
                    print("Sorry! You typed a number, but we need a letter! Try again!")
                    continue
            else:
                print("Sorry! There was an error while you were inputing your account details.")
                print("Exiting in 3 seconds.")
                print("FATAL: unknown error")
                sys.exit(3)
            for i in range(5):
                try:
                    pwd = input("Please input your Microsoft account password.\n-->")
                    break
                except:
                    print("Sorry! You typed a number, but we need a letter! Try again!")
                    continue
            else:
                print("Sorry! There was an error you were inputing your account details.")
                print("Exiting in 3 seconds.")
                print("FATAL: unknown error")
                sys.exit(3)
            
except:
    print("A fatal error occured!! We need to exit. Try rerunning the program. :(")
    print("FATAL: unknown error")
    print("System will exit in 3 seconds")
    time.sleep(3)
    sys.exit()

#dont change these lists, except for adding more verbs to verblist
#formula for how many possible searches: multiply the len of each list by each other (except searchlist)
startlist = ['why', 'how', 'what', 'where', 'when', 'who',]
auxlist = ['do', 'is', 'did', 'will', 'has', 'does']
subjectlist = ['you', 'i', 'we']
verblist = ['study', 'like', 'do', 'love', 'change', 'find', 'create', 'build']

# Obselete code, using wordlist.pkl now, which contains thousands of lines of words.
'''#add any nouns you want to infolist; it gives the bot more content to work with
infolist = ['dogs', 'microsoft', 'cars', 'food', 'walmart', 'grammarly', 'california', 'debate', 'monitor', 'paper', 'marvel', 'dc', 'tesla', 'dream', 'python', 'github', 'ram', 'ford', 'strike', 'amazon', 'aws']'''

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
        # Loading animation
        done = False
        t1 = threading.Thread(target = animated_marker)
        t1.start()
        # Login for the first webdriver instance
        driver.get('https://login.live.com')
        # Wait for email field and enter email
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
        # Click Next
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        # Wait for password field and enter password
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(pwd)
        # Click Login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        # Click Yes
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        time.sleep(1)
        done = True
        break
    except:
        print("Weird, the login didnt work. We'll try again.")
        continue
else:
    print("There were some issues getting you logged into your account. We tried several times, but we couldn't get it to work. :(")
    print("We'll continue on with the searches, but you won't be signed in.")
time.sleep(4)
# For loops to create two instances running at once
searchNumR(searchNum, timeNum)
# Click the sign in button after the bing searches are complete...
# Since they don't always sign in after the earlier bit of code
time.sleep(4)
#id = driver.find_element(By.ID, "id_a")
#id.click()
driver.close()
print("\nSearches completed succsesfully! Thanks again for using our bot!")