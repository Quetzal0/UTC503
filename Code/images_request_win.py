import os, ssl
from time import sleep
import requests
from bs4 import BeautifulSoup
import urllib.request

os.system('cls')
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def getdata(url):
    r = requests.get(url)
    return r.text

#get images description from HTML
def images_description():
    htmldata = getdata('https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432')
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img',  attrs={'class': 'img-fluid'})
    with open('your_path_here\\UTC503\\References\\alt.txt', 'a', encoding="utf-8") as f:
        for item in images:
            if ('mini' in item['src']):
                newline = item['alt'] + '\n'
                f.write(str(newline))

#download images from HTML
def download_images():
    htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432")
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img',  attrs={'class': 'img-fluid'})
    number = 10
    for item in images:
        if ('mini' in item['src']):
            jpg = str(number) + '.jpg'
            urllib.request.urlretrieve(item['src'], jpg)
            number += 1
            os.system('cls')
            print(f'Downloading images :\n\nDownloaded : {jpg}')
    images_description()
    sleep(1)
    print('Download done')