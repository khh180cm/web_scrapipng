import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import csv

########################
### Selenium setting ###
########################
service = Service('/Users/khh180cm/Downloads/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
starbucks_url = 'https://www.starbucks.co.kr/menu/drink_list.do' 
driver.get(starbucks_url)
# Scroll down : to get loading data(img, video, etc)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(1)

########################
# BeautifulSoup setting#
########################
name_beverage = []
img_beverage = []
soup = BeautifulSoup(driver.page_source, 'lxml')
for beverage in soup.find_all('a', class_='goDrinkView'):
	name_beverage.append(beverage.img['alt'])
	each_img = (beverage.img['src']).split('//')[1]
	img_beverage.append(each_img)
cnt = [x for x in range(1, len(name_beverage)+1)]
total_data = tuple(zip(cnt, name_beverage, img_beverage))	

########################
####### csv write ######
########################
file_name = 'Starbucks_menu.csv'
f = open(file_name, 'w+', encoding='utf-8', newline='')
wr = csv.writer(f)                                                     
wr.writerow(['No', '음료', '사진'])
for i in range(len(name_beverage)):
	wr.writerow(total_data[i])
f.close()                                                              
print(f'{file_name} 작업이 완료되었습니다. csv파일을 확인하세요.') 
driver.quit()
