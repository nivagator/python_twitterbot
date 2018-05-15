import tweepy
from time import sleep
from credentials import *
from datetime import datetime,timedelta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def retweet(q, interval, loops):
	t = datetime.now()
	today = t.strftime('%Y-%m-%d')
	lw = datetime.now() - timedelta(days=5)
	lastwk = lw.strftime('%Y-%m-%d')

	print('start')
	for tweet in tweepy.Cursor(api.search,q=q,since=lastwk,until=today,lang='en').items(loops):
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

def tweet(filename):
	my_file = open(filename, 'r')
	file_lines = my_file.readlines()
	my_file.close()
	for line in file_lines:
		try:
			print(line)
			if line != '\n':
				api.update_status(line)
				sleep(15)
			else: 
				pass
	
		except tweepy.TweepError as e:
			print(e.reason)
			sleep(2)



