'''this file is gonna post images downloaded from <images_request.py>'''
import random
import tweepy
import requests
import config
from images_request_win import download_images

class Connection:
    '''This class start the connection with the twitter account'''
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        print('Twitter Authentication Ok\n')
    except:
        print('Error during authentication\n')

def getdata_html(url):
    '''This function get HTML content from the url'''
    r = requests.get(url) 
    return r.text 

def history():
    '''This function check history of posts and
    change image to publish if it's already posted'''
    #The random number is used to select the file to pusblish from
    #downloaded images the Code/ folder (numbered from 10 to 45).
    random_num = random.randrange(10, 45)
    #This array store all the line from history.txt.
    history_line_array = []
    with open('your_path_here\\UTC503\\References\\history.txt', 'r') as f:
        for line in f:
            num_in = line
            history_line_array.append(int(num_in))
        #Regenerate the random number while it's in the history.txt.
        while random_num in history_line_array:
            random_num = random.randrange(10, 45)
    try:
        i = history_line_array[1]
        print(f'Images already downloaded {i} \n')
    except:
        download_images()
    return random_num

def publish():
    '''This function publish the selected image on the Twitter account'''
    random_num = history()
    #newline will fill history.txt.
    newline = '\n' + str(random_num)
    #This array store all the image descriptions from alt.txt.
    alt_array = []
    with open('your_path_here\\UTC503\\References\\history.txt', 'a') as f:
        f.write(str(newline))
    with open('your_path_here\\UTC503\\References\\alt.txt', 'r', encoding="utf-8") as f:
        i = 0
        for line in f:
            alt_array.append(line)
            i = i + 1
    #alt_index is 10 less than random_num because .jpg files starts at 10
    #and the alt.txt lines strats at 0.
    alt_index = random_num - 10
    #status is the text that will be posted with the image.
    status = alt_array[alt_index]
    #image path is the path from the image that will be posted.
    image_path = str(random_num) + '.jpg'
    #this line will post a tweet with an image and status.
    Connection.api.update_with_media(image_path, status)
    print(f'Posted :  {str(random_num)}  {alt_array[alt_index]}')
    return 0

if __name__ == "__main__":
    publish()