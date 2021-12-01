import requests
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime

date = datetime.now()

def getdata(url): 
    r = requests.get(url) 
    return r.text 

htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432") 
soup = BeautifulSoup(htmldata, 'html.parser') 
image = soup.find('img',  attrs={'class': 'image-large'}) 	

day = str(date).split(" ")

filename = "bronze_" + str(day[0] + ".jpg")

print(filename)

urllib.request.urlretrieve(image['src'], str(filename))
print(image['src'])