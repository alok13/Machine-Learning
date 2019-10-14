import tweepy
from textblob import TextBlob

## Predicting analysis and sentiment from series of tweets
consumer_key='1'
consumer_secret='1'

access_token ='143710382-1'
access_token_secret='1'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
