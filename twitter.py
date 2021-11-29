import requests
from bs4 import BeautifulSoup
import urllib.request

def getdata(url): 
    r = requests.get(url) 
    return r.text 

htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432") 
soup = BeautifulSoup(htmldata, 'html.parser') 
images = soup.find_all('img',  attrs={'class': 'img-fluid'}) 	

for item in images:
    print(item['src'])