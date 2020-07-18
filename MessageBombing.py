from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import urllib.parse
import urllib.error
import time


msg = '''Scammer'''
print(msg)

contact_number = input("Enter Number: ")
StartTime = time.time()
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(10)  # Wait period for you to log-in
serviceurl = "https://web.whatsapp.com/"
params = dict()
params['text'] = msg
url = serviceurl + 'send?phone=91' + contact_number + '&' + \
    urllib.parse.urlencode(params) + "&source&data&app_absent"
print(url)
driver.get(url)
time.sleep(3)

driver.find_element_by_xpath(
    "//*[@id='main']/footer/div[1]/div[3]/button").click()
for i in range(0, 1000):  # you can increase or decrease the number of messages by changing 1000
    WebElement = driver.find_element_by_xpath(
        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    WebElement.send_keys(msg)
    WebElement.send_keys(Keys.ENTER)
driver.quit()
