import requests
from bs4 import BeautifulSoup
import urllib.request
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


def getdata(url): 
    r = requests.get(url) 
    return r.text 

def download_images():
    htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    images = soup.find_all('img',  attrs={'class': 'img-fluid'})

    number = 10

    for item in images:
        if ('mini' in item['src']):
            jpg = str(number) + '.jpg'
            urllib.request.urlretrieve(item['src'], jpg)
            print(item['src'])
            number += 1

download_images()