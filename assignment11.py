#A11_Q1
"An access token is an object encapsulating the security identity of a process or thread.A token is used to make security decisions and to store tamper-proof information about some system entity."
#STEPS TO ACCESS TOKEN FOR API
#CREATE TWITTER ACCOUNT THEN GO TO TWITTER'S DEVELOPER PAGE
#THEN CREATE APPLICATION AND ADD DETAILS LIKE APPLICATION NAME,DESCRIPTION AND WEBSITE NAME AND CREATE TWITTER APPLICATION
#NOW GO TO KEYS AND TOKEN AND CLICK ON GENERATE ACCESS TOKEN


#A11_Q2
#Domain Name	=www.google.com
#IP Address	=172.217.15.100
#Google Inc.(AS15169)



#Domain Name	=acadview.com
#IP Address	=52.37.66.135
#Amazon.com, Inc. (AS16509)

#A11_Q3
from keys import Consumer_Key,Consumer_Secret,Access_Token,AccessToken_Secret
import tweepy

oauth=tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
oauth.set_access_token(Access_Token,AccessToken_Secret)
api=tweepy.API(oauth)
print(api.search("#modi"))
user=api.get_user("navpreetsingh")
print(user.screen_name)
print(user.followers_count)

#A11_Q4
#A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)
#An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)


#Library: android.app.Activity library (Class with all code)
#API: Android API to interact with hardware, like the front camera of an Android-based device. If your app needs to vibrate the phone, you must use the Android API method like vibratePhone()


#A11_Q5
from keys import Consumer_Key,Consumer_Secret,Access_Token,AccessToken_Secret
import tweepy

oauth=tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
oauth.set_access_token(Access_Token,AccessToken_Secret)
api=tweepy.API(oauth)
user=api.get_user("#modi")
print(user.screen_name)
print(api.retweets_of_me)
