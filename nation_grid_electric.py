from selenium import webdriver
import time
import re
import os
from datetime import datetime as dt
from json_update import json_update as js_update
from sendemail import send_mail as se

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *
class National_Electric:
        
    def __init__(self):
        pass

    def run(self):
        path = r"browser_exe/chromedriver.exe"
        website = 'https://www1.nationalgridus.com/SignIn'
        browser = webdriver.Chrome(path)
        browser.set_page_load_timeout(10)
        browser.get(website)

        ##wait = WebDriverWait(browser, 10)
        browser.find_element_by_xpath('//*[@id="modalWrapper"]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li[1]/a').click()
        browser.set_page_load_timeout(10)
        browser.find_element_by_xpath('//*[@id="modalWrapper"]/div[2]/div/div[1]/div[2]/ul/li[1]/a/span').click()
        ##browser.maximize_window()
        time.sleep(10)
        ##wait = WebDriverWait(browser, 20)
        ##element = wait.until(EC.presence_of_element_located((By.NAME, "ctl00$ctl00$c1$MainContent$UCSignIn$txtSigninID")))
        ##print(element)
        ##if element:
        browser.find_element_by_id('c1_MainContent_UCSignIn_txtSigninID').send_keys(Username_Electric)
        browser.find_element_by_name('ctl00$ctl00$c1$MainContent$UCSignIn$txtPassword').send_keys(Password)
        browser.set_page_load_timeout(10)
        browser.find_element_by_id('c1_MainContent_UCSignIn_btnSignin').click()

        browser.set_page_load_timeout(30)
        data = browser.find_element_by_xpath('//*[@id="twContent"]/div[2]/ul/li[1]')

        lookup = str(data.text)
        balance = re.search(r'(\d+(?:\.\d{2})?)',lookup).group(0)
        print("Account Balance: " + balance)
        due = re.search(r'\d{2}/\d{2}[/]\d{4}',lookup).group(0)
        print('Due Date: ' + due)
        #COnvert to time format to check if we have the record already.
        a = dt.strptime(due,"%m/%d/%Y")

        try:
            rfile = open('National_Electric.txt','r')
        except:
            rfile = open('National_Electric.txt','w')
            rfile.close()
        rfile = open('National_Electric.txt','r')
        read_file = rfile.read()
        rfile.close()

            
        if due not in read_file and float(balance) != 0.00:
            file = open('National_Electric.txt','a')
            file.write('-'*30 + '\n')
            file.write("Account Balance: " + balance + '\n')
            file.write('Due Date: ' + due + '\n')
            file.close()

            js_update(float(balance),due,"Electric")
            se(balance,due,'Electric',website)

        ##browser.find_element_by_class_name("lsb").click()
        time.sleep(4)
        browser.quit()
