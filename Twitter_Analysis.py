import tweepy
from textblob import TextBlob

## Predicting analysis and sentiment from series of tweets
consumer_key='AS3kobyASHOimBqvzMwvVmFWf'
consumer_secret='cQveuw0EpNJUZWK3PVGP9M1BO0FCJEUXCWHhc6pZRtajJzLvIB'

access_token ='143710382-Ql1RDJHk0J31MRofPIINtRzn0jI4sqVTfPst6TIC'
access_token_secret='LWX1PadDfZp0wxkUWFOC5HB30tLt3b6CpKRaSb0Ta0cKd'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)