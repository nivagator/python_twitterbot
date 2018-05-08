import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def retweet(q, interval):
	print('start')
	for tweet in tweepy.Cursor(api.search,q=q,lang='en').items(10):
		try:
			print('\nTweet by: @' + tweet.user.screen_name)
			tweet.retweet()
			print('Retweeted the tweet')

			if not tweet.user.following:
				tweet.user.follow()
				print('Followed the user')
			else:
				print('already following')

			sleep(interval)

		except tweepy.TweepError as e:
			print(e.reason)

		except StopIteration:
			break

