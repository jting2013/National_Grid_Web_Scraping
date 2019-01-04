from selenium import webdriver
import time
from json_update import json_update as js_update
from sendemail import send_mail as se

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from config import *
class National_Gas:
    def __init__(self):
        pass

    def run(self):
        print(Username)
        path = r"browser_exe/chromedriver.exe"
        website = 'https://online.nationalgridus.com/login/LoginActivate?applicurl=aHR0cHM6Ly9vbmxpbmUubmF0aW9uYWxncmlkdXMuY29tL2VzZXJ2aWNlX2VudQ==&auth_method=0'
        browser = webdriver.Chrome(path)
        browser.set_page_load_timeout(10)
        browser.get(website)
        ##browser.maximize_window()
        ##wait = WebDriverWait(browser, 10)
        browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/table[5]/tbody/tr[2]/td[1]/form/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/input').send_keys(Username)
        browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/table[5]/tbody/tr[2]/td[1]/form/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td[2]/input').send_keys(Password)
        try:
            browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/table[5]/tbody/tr[2]/td[1]/form/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[1]/input').click()
            print('bad')
            browser.set_page_load_timeout(10)
        except:
            print('catch')
            browser.refresh()
        browser.set_page_load_timeout(10)
        parent = browser.find_element_by_name('_sweclient')
        browser.switch_to_frame(parent)
        child = browser.find_element_by_name('_sweview')
        browser.switch_to_frame(child)

        value = browser.find_element_by_xpath('//*[@id="s_4_1_15_0"]').text
        print('Account Balance: ' + value)
        date = browser.find_element_by_xpath('//*[@id="s_4_1_17_0"]').text
        print('Last date: ' + date)
        balance = value.split('$')[1]

        try:
            rfile = open('National_Gas.txt','r')
        except:
            rfile = open('National_Gas.txt','w')
            rfile.close()
        rfile = open('National_Gas.txt','r')
        read_file = rfile.read()
        rfile.close()          

        if date not in read_file and float(balance) != 0.00:
            file = open('National_Gas.txt','a')
            file.write('-'*30 + '\n')
            file.write("Account Balance: " + value + '\n')
            file.write('Date: ' + date + '\n')
            file.close()
            js_update(float(balance),date,"Gas")
            se(value,date,'Gas',website)
            
        time.sleep(4)
        browser.quit()
