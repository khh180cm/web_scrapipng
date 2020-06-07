from bs4 import BeautifulSoup
import requests 
import csv

page = requests.get('https://www.billboard.com/charts/hot-100')
soup = BeautifulSoup(page.text,'html.parser')

# Element parsing for billboard Top 10
ranks = soup.find_all('span', {'chart-element__rank__number'})
song_names = soup.find_all('span',{'class':'chart-element__information__song text--truncate color--primary'})
singers = soup.find_all('span', {'class':'chart-element__information__artist text--truncate color--secondary'})   
length = len(singers)
for i in range(length):
	 ranks[i] = ranks[i].get_text()
	 song_names[i] = song_names[i].get_text()
	 singers[i] = singers[i].get_text()
total_info = tuple(zip(ranks, song_names, singers))
	
#write a csv file
f = open('billboard_top_100.csv', 'w+', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['순위', '노래','아티스트'])
for i in range(length):
	wr.writerow(total_info[i])
f.close()    


