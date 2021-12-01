import requests
from bs4 import BeautifulSoup
import urllib.request

def getdata(url): 
    r = requests.get(url) 
    return r.text 

htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432") 
soup = BeautifulSoup(htmldata, 'html.parser') 
images = soup.find_all('img',  attrs={'class': 'img-fluid'}) 	

number = 0

for item in images:
    urllib.request.urlretrieve(item['src'], str(number))
    print(item['src'])
    number += 1