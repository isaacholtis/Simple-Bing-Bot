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

# Using firefox, since Microsoft Edge was not letting me sign in
whatBrowse = webdriver.Firefox()
whatBrowse2 = webdriver.Firefox()
# Email web content on the Microsoft account page
EMAILFIELD = (By.ID, "i0116")
# Password web content on the Microsoft account page
PASSWORDFIELD = (By.ID, "i0118")
# Next button content on the Microsoft account page
NEXTBUTTON = (By.ID, "idSIButton9")
with open('encEPwd.pkl', 'rb') as encOpenEmail:
    encFiles = pickle.load(encOpenEmail)
with open('encKey.pkl', 'rb') as encOpenKey:
    encFilesKey = pickle.load(encOpenKey)
# Get a variable to tell the system how many tabs to open.
searchNum = int(input("Please input the number of searches you want completed.\nEach search will open a tab once, and then close that tab, so feel free to do as many as you want!\n-->"))
# Get a variable to tell the system how long to wait before closing a tab.
timeNum = int(input("Please input how long you'd like to wait between searches.\nToo short of a time may cause the page to fail to load.\n-->"))
tabNum = int(input("Please input how many tabs you'd like open at once.\n-->"))
userName = input("Please input your first and last name so we can store you encrypted username and password.\nIf you've already entered your email and password once, then put in your name, and we'll load your profile\n-->")
if userName + " Email" in encFiles:
    print("You exist in our system! Logging you in now!")
    emailCrypt = encFiles[userName + " Email"]
    emailKey = encFilesKey[userName + " keyEmail"]
    email = emailKey.decrypt(emailCrypt).decode()
    pwdCrypt = encFiles[userName + " Password"]
    pwdKey = encFilesKey[userName + " keyPwd"]
    pwd = pwdKey.decrypt(pwdCrypt).decode()
else:
    email = input("Please enter you Microsoft account email.\n-->")
    pwd = input("Please input your Microsoft account password.\n-->")
    key = Fernet.generate_key()
    key2 = Fernet.generate_key()
    keyEmail = Fernet(key)
    keyPwd = Fernet(key2)
    encEmail = keyEmail.encrypt(email.encode())
    encPwd = keyPwd.encrypt(pwd.encode())
    # Pickle file for the encrypted email and password
    encEPPickle = {userName + " Email": encEmail, userName + " Password": encPwd}
    with open('encEPwd.pkl', 'wb') as encFile:
        pickle.dump(encEPPickle, encFile)
    # Pickle file for the encryption key
    encKeyPickle = {userName + " keyEmail": keyEmail, userName + " keyPwd": keyPwd}
    with open('encKey.pkl', 'wb') as encKey:
        pickle.dump(encKeyPickle, encKey)
def searchNumR(n1,n2, t1):
    for i in range(n1):
        t1.get(f"https://www.bing.com/search?q={randint(1,2000)}")
        time.sleep(n2)
        print("This thread is running fine, and the tab was closed.")

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
WebDriverWait(whatBrowse, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
time.sleep(1)
# Login for the second webdriver instance
whatBrowse2.get('https://login.live.com')
# Wait for email field and enter email
WebDriverWait(whatBrowse2, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)
# Click Next
WebDriverWait(whatBrowse2, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
# Wait for password field and enter password
WebDriverWait(whatBrowse2, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(pwd)
# Click Login
WebDriverWait(whatBrowse2, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
WebDriverWait(whatBrowse2, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
time.sleep(4)
# For loops to create two instances running at once.
for i in range(tabNum):
    i = threading.Thread(target=searchNumR, args=(searchNum,timeNum,whatBrowse))
    i.start()
for i in range(tabNum):
    i = threading.Thread(target=searchNumR, args=(searchNum,timeNum,whatBrowse2))
    i.start()