import requests
from bs4 import BeautifulSoup
import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=4)

responce=requests.get('https://www.imdb.com/search/title/?release_date=2017-01-01,2020-12-31')

soup=BeautifulSoup(responce.text,"lxml")

article = soup.find('div', attrs={'class': 'article'}).find('h1')

i=1
top50movie={}
movielist={
    'serialNo':'',
    'name': '',
    'certificate': '',
    'description': '',
    'stars': [],
    'runTime':''
}
movieList = soup.findAll('div', attrs={'class': 'lister-item-content'})
for div_item in (movieList):
     movielist={}
     top50movie[i]=movielist
     p_list=div_item.findAll('p')
     movielist['runTime']=p_list[0].find('span',{'class':'runtime'})
     movielist['serialNo']=str(i)
     head = div_item.findChildren('h3',attrs={'class':'lister-item-header'})
     movielist['name']=str((head[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore'))
     movielist['description']=str((p_list[1].text.strip()))
     print(movielist)
     i += 1

p=pd.DataFrame(top50movie)
p.to_csv('file.csv')
pp.pprint(top50movie)