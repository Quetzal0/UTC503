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


#check history of posts
def history():
    is_in = 'none'
    random_num = random.randrange(10, 46)#ATTENTION
    line_array = []
    with open('D:\\Code\\Python\\non_py\\history.txt', 'r') as f:
        for line in f:
            num_in = int(line)
            line_array.append(num_in)
        f.close
        while random_num in line_array:
            random_num = random.randrange(10, 46)#ATTENTION
    return random_num

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
    random_num = history()
    newline = '\n' + str(random_num)

    #publish images
    with open('D:\\Code\\Python\\non_py\\history.txt', 'a') as f:
        f.write(str(newline))
        images_description()
        index = random_num - 10
        status = alt_array[index]
        image_path = 'D:\\Code\\Python\\UTC503\\' + str(random_num) + '.jpg'
        #Connection.api.update_with_media(image_path, status)
        print('Posted : ' + str(random_num) + ' ' + alt_array[index])
        return 0

publish()
