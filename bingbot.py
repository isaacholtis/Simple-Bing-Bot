
from random import randint
import time
import threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from cryptography.fernet import Fernet
import pickle
import sys
from os import startfile

print("Starting browser, give us a moment.")
# Using firefox, since Microsoft Edge was not letting me sign in
whatBrowse = webdriver.Firefox()
print("Browser started")

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
        # Loads the pickle files with the user dictionarys 
        with open('encEPwd.pkl', 'rb') as encOpenEmail:
            encFiles = pickle.load(encOpenEmail)
        with open('encKey.pkl', 'rb') as encOpenKey:
            encFilesKey = pickle.load(encOpenKey)
        break
    except FileNotFoundError:
        print("We couldn't load the user data base file. If you have entered your credentials before, we can try to load the database agian.\nIf you are a new user, you can skip this step, and continue the process.")
        tryAgian = input("Would you like us to try again? Type yes or no.\n-->")
        if str.lower(tryAgian) == "yes":
            continue
        else:
            break
    except pickle.PickleError:
        print("We couldn't load the user data base file. If you have entered your credentials before, we can try to load the database agian.\nIf you are a new user, you can skip this step, and continue the process.")
        tryAgian = input("Would you like us to try again? Type yes or no.\n-->")
        if str.lower(tryAgian) == "yes":
            continue
        else:
            break
else:
    print("Looks like we've hit an error loading the user data base files that we can't resolve. We'll have to close the program. :(")
    startfile("ErrorHandler.txt")
    print("System will exit in 3 seconds")
    time.sleep(2.9)
    sys.exit()
# Get a variable to tell the system how many searches each thread completes...
# This will be double the searches intended by the user, so we need to fix that
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
    startfile("ErrorHandler.txt")
    print("System will exit in 3 seconds")
    time.sleep(2.9)
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
    startfile("ErrorHandler.txt")
    print("System will exit in 3 seconds")
    time.sleep(2.9)
    sys.exit()
# Gets the name of the user, so we can check if they have entered their credentials before
for i in range(5):
    try:
        userName = input("Please input your first and last name so we can store you encrypted username and password.\nIf you've already entered your email and password once, then put in your name, and we'll load your profile\n-->")
    except ValueError:
        print("You didn't type letters!\n\nTry again!\n")
        continue
    else:
        break
else:
    print("You did something wrong too many times. Try rerunning the program. :(")
    startfile("ErrorHandler.txt")
    print("System will exit in 3 seconds")
    time.sleep(2.9)
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
        email = input("Please enter you Microsoft account email.\n-->")
        pwd = input("Please input your Microsoft account password.\n-->")
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
        # Store the dictionary in a pickle file called encEPwd.pkl
        with open('encEPwd.pkl', 'wb') as encFile:
            pickle.dump(encEPPickle, encFile)
        # Dictionary that will be stored in a pickle file...
        #  with the decryption keys for the email and password in it with appropriate dictionary...
        #  keys to call back the decryption keys later
        encKeyPickle = {userName + " keyEmail": keyEmail, userName + " keyPwd": keyPwd}
        with open('encKey.pkl', 'wb') as encKey:
            pickle.dump(encKeyPickle, encKey)
        print("Profile saved succesesfully!\nJust type your name next time you use the bot, and we'll remember you password.\nAnd of course, it also encypted.")
except:
    print("A fatal error occured!! We need to exit. Try rerunning the program. :(")
    startfile("ErrorHandler.txt")
    print("System will exit in 3 seconds")
    time.sleep(2.9)
    sys.exit()

# Defines the funtion that the threads use later on to search...
# t1 represents which WebDriver that thread uses, the first or the second one...
# You need to WebDrivers because you can't control more than one tab at a time...
# I think we should make a for loop that desides how many WebDriver instances you would have...
# but that would be burdensome to implement
def searchNumR(n1,n2, t1):
    for i in range(n1):
        t1.get(f"https://www.bing.com/search?q={randint(1,2000)}")
        time.sleep(n2)
        print("This thread is running fine, and the tab was closed.")
for i in range(5):
    try:
        # Login for the first webdriver instance
        whatBrowse.get('https://login.live.com')
        # Wait for email field and enter email
        WebDriverWait(whatBrowse, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
        # Click Next
        WebDriverWait(whatBrowse, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        # Wait for password field and enter password
        WebDriverWait(whatBrowse, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(pwd)
        # Click Login
        WebDriverWait(whatBrowse, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        # Click Yes
        WebDriverWait(whatBrowse, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
        time.sleep(1)
        break
    except:
        print("Weird, the login didnt work. We'll try again.")
        continue
else:
    print("There were some issues getting you logged into your account. We tried several times, but we couldn't get it to work.\nThe program will have to close. :(")
    startfile("ErrorHandler.txt")
    print("System will exit in 3 seconds")
    time.sleep(2.9)
    sys.exit()
time.sleep(4)
# For loops to create two instances running at once
searchNumR(searchNum, timeNum, whatBrowse)
# Click the sign in button after the bing searches are complete...
# Since they don't always sign in after the earlier bit of code
time.sleep(4)
id = whatBrowse.find_element_by_id("id_a")
id.click()
print("Searches completed succsesfully! Thanks again for using our bot!")