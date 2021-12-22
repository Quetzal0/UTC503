from re import X
import tweepy
import requests
from bs4 import BeautifulSoup
import random
import config

#images description array
alt_array = []

#connection to twitter
class Connection:
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        print('Authentication OK')
    except:
        print('Error during authentication')

#get HTML data from URL
def getdata_html(url): 
    r = requests.get(url) 
    return r.text 

#get images description from HTML
def images_description():
    htmldata = getdata_html('https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432') 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    images = soup.find_all('img',  attrs={'class': 'img-fluid'})

    number = 10

    for item in images:
        if ('mini' in item['src']):
            alt_array.append(item['alt'])
            number += 1

#publish downloaded images with description
def publish():

    random_num = random.randrange(10, 46)
    print(random_num)

    newline = '\n' + str(random_num)

    is_in = ''

    #check history of posts
    with open('D:\\Code\\Python\\non_py\\history.txt', 'r') as f:
        for line in f:
            if str(random_num) in line:
                is_in = 'true'
                print(random_num)
            else : 
                pass
    f.close

    if is_in == 'true':
        print('already posted')
    
    #publish images
    else:
        with open('D:\\Code\\Python\\non_py\\history.txt', 'a') as f:
            f.write(str(newline))
            images_description()
            index = random_num - 10
            status = alt_array[index]
            image_path = 'D:\\Code\\Python\\UTC503\\' + str(random_num) + '.jpg'
            status = Connection.api.update_with_media(image_path, status)
            print('Posted')

publish()