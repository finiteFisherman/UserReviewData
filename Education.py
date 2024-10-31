import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# instantiate options
options = webdriver.ChromeOptions()

# run browser in headless mode
options.headless = True

# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# load website
url = "https://www.zhihu.com/consult/people/1095738760850989056?hideHomeBar=1"

# get the entire website content
driver.get(url)

#select elements by class name
# if one line BaseInfoCard-badges otherwise BaseInfoCard-badges"][1] and BaseInfoCard-badges"][2]
name = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-name"]').text
#homeURL = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-homeUrl"]').text
baseInfoCardBadge = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-badges"]').text
#baseInfoCardBadge1 = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-badges"][1]').text
#baseInfoCardBadge2 = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-badges"][2]').text
baseInfoCardDesc = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-desc"]').text
baseInfoCardAvgInfo = driver.find_element(By.XPATH, '//div[@class="BaseInfoCard-avgInfo"]').text
ConvServRoot = driver.find_element(By.XPATH, '//div[@class="ConversationService-root"]').text
#questionUser = driver.find_element(By.XPATH, '//div[@class="PublicConsultation-list"]').text


dictionary1 =({
    "Name": name,
    #"URL": homeURL,
    "Base Info Card Badge": baseInfoCardBadge,
    #"Base Info Card Badge1": baseInfoCardBadge1,
    #"Base Info Card Badge2": baseInfoCardBadge2,
    "Base Info Desc": baseInfoCardDesc,
    "Base Info Card - Avg Info": baseInfoCardAvgInfo,
    "Conversation Service Root": ConvServRoot,
    #"Question User": questionUser                #public question

})

# print elements
print(dictionary1)
dictionary1.get("Name")
dictionary1.get("Base Info Card Badge")
#dictionary1.get("Base Info Card Badge1")
#dictionary1.get("Base Info Card Badge2")
dictionary1.get("Base Info Desc")
dictionary1.get("Base Info Card - Avg Info")
dictionary1.get("Conversation Service Root")


# #Serializing json
# json_object = json.dumps(dictionary, indent=8)
# # Writing to sample.json
# with open("C:/Users/dsl89/Documents/spring24/gradAssistant/testPython/sample.json", "w") as outfile:
#     outfile.write(json_object)

driver.close()

