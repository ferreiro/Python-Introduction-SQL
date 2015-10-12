import tweepy
import time

#insert your Twitter keys here
consumer_key = "lEHqqXbOPLQ2KdkBZ6tTZZmwu",
consumer_secret = "hDM9vphywDOiIHvLQRVEt7cr3qor8kuet4QTKO3kubZXOwm6Tb",
access_token = "332470891-BYQMmINu1ve5c0va7BIH8RwPe1ldAUkiDLDKyVCx",
access_secret = "G5eqn38B7BswVK19u06sJOAepMMl7yFteIsGT0CmMUEYj"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

list= open('list.txt','w')

if(api.verify_credentials):
    print 'We sucessfully logged in'

user = tweepy.Cursor(api.followers, screen_name="arabbankgroup").items()

while True:
    try:
        u = next(user)
        list.write(u.screen_name +' \n')

    except:
        time.sleep(15*60)
        print 'We got a timeout ... Sleeping for 15 minutes'
        u = next(user)
        list.write(u.screen_name +' \n')
list.close()