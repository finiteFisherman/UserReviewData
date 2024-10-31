import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd
import json


# throtling
y = random.randint(1,3)
x = random.random()
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
urls = "https://www.zhihu.com/consult/conversation/1647768323461988353/archive?showIWantConsult=1&showFixedBtn=1"

r = requests.get(url=urls)
soup = BeautifulSoup(r.content, "html.parser")

# Questions Pages
values = []
dateList = []
myLi = soup.find_all("span", {"class": "ArchiveExtraInfo-value"})  # find Values, Observations, Likes
for i in myLi:
    values.append(i)
    print(i.get_text())

dates = soup.find("span", {"class": "Archive-messageDate"})  # date
for i in dates:
    dateList.append(i.get_text())
    print(i.get_text())

df2 = pd.DataFrame(data=values)
d = df2.transpose()
d["3"] = dateList  # add date
d.to_csv('C:/Users/dsl89/Documents/spring24/gradAssistant/testPython/workplace/User.csv', sep=',', index=True,
         header=True)

print('sleep now', time.ctime())
time.sleep(x + y)
print('wake up', time.ctime())
