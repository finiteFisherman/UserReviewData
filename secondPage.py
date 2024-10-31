from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# handles opening all public consultant questions with click and scroll then save html

#Random double for sleeps
num = 1
sleepNum = num+random.random()
print("First Sleep Time is: ", sleepNum)

# instantiate options
options = webdriver.ChromeOptions()

# run browser in headless mode
options.headless = True

# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# load website
url = "https://www.zhihu.com/consult/people/931304910375514112?hideHomeBar=1"

# get the entire website content
driver.get(url)

driver.maximize_window()
# Scroll to bottom
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(num+random.random())

#click on object
l= driver.find_element(By.XPATH,"//div[@class='PublicConsultation-layerContent']")
#perform actual click action
l.click()
time.sleep(num+random.random())

#Keep scrolling, clicking

itemTargetCount = 200
counter =0
while counter<=itemTargetCount:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(num + random.random())
    l.click()
    time.sleep(num + random.random())
    counter=counter+1
    print("Num Clicks: ", counter)


driver.close()