from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

a="https://www.railway.gov.tw/tra-tip-web/tip"
driver = webdriver.Chrome()
driver.get(a)
time.sleep(5)
strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[1]/div[2]/input"
# name = '//*[@name="account"]'
driver.find_element(By.XPATH,strr).send_keys(['台','北'])
time.sleep(5)
strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[3]/div[2]/input"
# name = '//*[@name="account"]'
driver.find_element(By.XPATH,strr).send_keys(['高','雄'])
time.sleep(5)
strr ="/html/body/div[6]/div[4]/div/div[1]/form/div[6]/input"
driver.find_element(By.XPATH,strr).click()
time.sleep(5)

table=driver.find_element(By.TAG_NAME,"table")
rows=table.find_elements(By.CLASS_NAME,"trip-column")
for row in rows:
    train=row.find_element(By.CLASS_NAME,"links")
    print(train.text)

while True:
    time.sleep(1)