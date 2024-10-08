from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)
url = "https://hk.on.cc/hk/bkn/cnt/news/20240927/bkn-20240927080347712-0927_00822_001.html"
driver.get(url)
search = driver.find_element(by=By.CSS_SELECTOR, value="div[class='topHeadline'] h1").text
print(search)
para = driver.find_element(by=By.CSS_SELECTOR, value="body > div:nth-child(19) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1)").text
print(para)
paragraph = driver.find_element(By.XPATH, "(//div[@class='paragraph'])").text
print(paragraph)
#search.send_keys("hello")
#search.send_keys(keys.ENTER)
#para.send_keys(keys.BACKSPACE)
time.sleep(3)
driver.close()
