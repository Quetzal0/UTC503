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
        print('Authentication OK\n')
    except:
        print('Error during authentication\n')

#get HTML data from URL
def getdata_html(url): 
    r = requests.get(url) 
    return r.text 

#check history of posts
def history():
    random_num = random.randrange(10, 45)#ATTENTION
    line_array = []
    with open('..\\References\\history.txt', 'r') as f:
        for line in f:
            num_in = line
            line_array.append(int(num_in))
        f.close
        while random_num in line_array:
            random_num = random.randrange(10, 45)#ATTENTION
    return random_num

#publish downloaded images with description
def publish():
    random_num = history()
    newline = '\n' + str(random_num)
    alt_array = []

    #publish images
    with open('..\\References\\history.txt', 'a') as f:
        f.write(str(newline))
        f.close
    with open('..\\References\\alt.txt', 'r', encoding="utf-8") as f:
        i = 0
        for line in f:
            alt_array.append(line)
            i = i + 1
        f.close
    
    index = random_num - 10
    status = alt_array[index]
    image_path = str(random_num) + '.jpg'
    #Connection.api.update_with_media(image_path, status)
    print(f'Posted :  {str(random_num)}  {alt_array[index]}')
    return 0

#main
def main():
    publish()

if __name__ == "__main__":
    main()
