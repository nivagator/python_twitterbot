from credentials import *
import tweepy
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_file = open('verne20.txt','r')
file_lines = my_file.readlines()
my_file.close()

def tweet():
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


