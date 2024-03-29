import requests
from bs4 import BeautifulSoup
import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from constants import *

class Streamer(webdriver.Chrome):

    def __init__(self,driver_path=r"C:\selenium_drivers",teardown=False) -> None:
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += driver_path
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        options.add_experimental_option("detach", True)
        super(Streamer,self).__init__(options=options,executable_path=os.environ.get("CHROMEDRIVER_PATH"))
        self.implicitly_wait(15)
 

    def __call__(self):

        self.get_page()
        time.sleep(2)
        button = self.get_button()
        # print(self)
        button.click()
        # self.execute_script("window.open('https://twitter.com/home','new window')")
        
        time.sleep(30)
        self.quit()
        
        

    
    def __exit__(self, *args):
        if self.teardown:
            self.quit()
        # return super().__exit__(*args)
    def get_page(self):
        self.get(BASE_URL)
    
    def get_button(self):
        # -1 0 11 12
        # 0 0 12 12
        WebDriverWait(self,30).until(
            EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Play or pause"]'))
        )
        button = self.find_element(By.XPATH, '//button[@aria-label="Play or pause"]')
        return button
    
        
        