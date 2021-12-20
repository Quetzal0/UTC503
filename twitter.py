import tweepy
import requests
from bs4 import BeautifulSoup
import urllib.request

CONSUMER_KEY = 'LCIQ6UDScOWyQgMzxkqs3xl3P'
CONSUMER_SECRET = 'SWetNtuZet5YWlPg91CYiB7HKAQS3yQnCDIWeJD0jSSlAJO4ai'
ACCESS_TOKEN = '1465336751090712576-4CP1mSDmTq9LC31zQDsfYaj9nrPDNY'
ACCESS_TOKEN_SECRET = 'H8RY13hE6kGkaOJsaatA9v1akoBkmOEJ6ryDmaK3dEB4H'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def getdata(url): 
    r = requests.get(url) 
    return r.text 

alt_array = []

def images_alt():
    htmldata = getdata("https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432") 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    images = soup.find_all('img',  attrs={'class': 'img-fluid'})

    number = 0

    for item in images:
        if ('mini' in item['src']):
            #print(item['alt'])
            alt_array.append(item['alt'])
            number += 1

images_alt()

#print(len(alt_array))

print(alt_array[1])


# the text to be tweeted
status = alt_array[31   ]

image_path = "D:\\Code\\Python\\UTC503\\31.jpg"
  
# posting the tweet
status = api.update_with_media(image_path, status)

# posting confirmation
print('Message posté')



