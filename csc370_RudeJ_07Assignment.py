#!/usr/bin/python
#
# CSC370 Assignemtn 07 Sentiment Analysis
# Version 1.0 
# By: Jordon Rude

#import dependencies, tweepy library for accessing twitter API
# textblob performs the actual sentiment analysis

import tweepy
from textblob import TextBlob

# import twitter API keys for authentication
consumer_key = '3Fg1MsvJ3ApJBb5lkVsgRRRGs' 
consumer_secret = 'S0Kae153W04yoAhq5fgNwdRBcb5pcJPPGkXlp1YH4QXyDB3jRZ'

access_token = '186934319-ESzq0N7PNvujJevFXKOLX4lJZunDnCC8keRKMARb'
access_token_secret= '1etrCZjDWMgJKx9gnLMZg6dtLaenzMdxPxjift0NnyiUz'

#authenticate to the twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#ask user input to set single argument
search = raw_input("Enter your subject to analyze: ")

#set single argument that makes a list of tweets
public_tweets = api.search(search)

# print the sentiment analysis of each tweet related to above text search
for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)


