from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request, urllib.parse, urllib.error
import time


msg = '''Yo!'''
print(msg)

contact_number = input("Enter Number: ")
StartTime = time.time()
driver = webdriver.Chrome(executable_path = "/mnt/e/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10) #Wait period for you to log-in
serviceurl = "https://wa.me/"
params = dict()
params['text'] = msg
url = serviceurl + '91' + contact_number + '/?' + urllib.parse.urlencode(params)
driver.get(url)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='action-button']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
for i in range(0, 1000): #you can increase or decrease the number by changing 1000
    WebElement = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    WebElement.send_keys(msg)
    WebElement.send_keys(Keys.ENTER)
driver.quit()
