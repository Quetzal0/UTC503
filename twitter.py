import json
import tweepy

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

# the text to be tweeted
status = "This is a tweet."
  
# posting the tweet
api.update_status(status)