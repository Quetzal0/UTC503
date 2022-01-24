from re import X
import tweepy
import requests
from bs4 import BeautifulSoup
import random
import config

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


#images description array
alt_array = []

#get HTML data from URL
def getdata_html(url): 
    r = requests.get(url) 
    return r.text 

#check history of posts
def history():
    is_in = 'none'
    random_num = random.randrange(10, 44)#ATTENTION
    line_array = []
    with open('history.txt', 'r') as f:
        for line in f:
            num_in = line
            line_array.append(num_in)
        f.close
        while random_num in line_array:
            random_num = random.randrange(10, 44)#ATTENTION
    return random_num

#publish downloaded images with description
def publish():
    random_num = history()
    newline = '\n' + str(random_num)

    #publish images
    with open('history.txt', 'a') as f:
        f.write(str(newline))
        f.close
    with open('alt.txt', 'r', encoding="utf-8") as f:
        i = 0
        for line in f:
            print(f'{i}  : {line}')
            alt_array.append(line)
            i = i + 1
        f.close
    
    index = random_num - 10
    status = alt_array[index]
    image_path = str(random_num) + '.jpg'
    Connection.api.update_with_media(status, image_path)
    #print(f'Posted :  {str(random_num)}  {alt_array[index]}')
    return 0
publish()
