import requests
from bs4 import BeautifulSoup
import urllib.request
from collections import Counter

url = "https://www.youtube.com/feed/explore"


def getdata(url): 
    r = requests.get(url) 
    return r.text 

htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art?onSale=1") 
soup = BeautifulSoup(htmldata, 'html.parser') 
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img',  attrs={ 'class': 'img-fluid'}) 	

for item in images:
    print(item['src']) 