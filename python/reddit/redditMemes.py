import praw
import os
import time
from urllib import request
import random
import json

reddit = praw.Reddit(client_id='B8ZEg7a304hCfw',
	client_secret='wWoLUJrIAWGbPddy3W0lzU7dVqw',
	user_agent='meme-machine:reddit-collector:v1.0 (by /u/theMusicalGamer88)')

def getMemes(args):
	subredditsFile = open(args.subReddits, "r")

	subreddits = []

	#read subreddit names from file into list "subreddits" as subreddit objects
	for line in subredditsFile.readlines():
		subreddits.append(reddit.subreddit(line.strip()))

	#for every subreddit, get Images
	urls = []
	titles = []
	dates = []
	ids = []
	for subreddit in subreddits:
		posts = getImagesFromSubreddit(subreddit, args)
		
		for url in posts[0]:
			urls.append(url)
		
		for date in posts[1]:
			dates.append(date)
	
	subreddit = getRandomSubreddit(subreddits)
	posts = getImagesFromSubreddit(subreddit, args)
	
	for url in posts[0]:
		urls.append(url)
	
	for date in posts[1]:
		dates.append(date)
	
	payload = {
		'memes': []
	}
	
	for i in range(args.urlNumber):
		meme = {}
		if 'http://imgur.com/' in urls[i][:17] and '.jpg' not in urls[i] and '.png' not in urls[i]:
			meme = {
				'imageUrl': urls[i] + '.png',
				'text0': None,
				'text1': None,
				'datePosted': dates[i],
				'datePulled': time.time(),
				'source': 'imgur',
				'filename': '{}.png'.format(dates[i])
			}
		else:
			if '.jpg' in urls[i]:
				meme = {
					'imageUrl': urls[i],
					'text0': None,
					'text1': None,
					'datePosted': dates[i],
					'datePulled': time.time(),
					'source': 'reddit',
					'filename': '{}.jpg'.format(dates[i])
				}
			elif '.png' in urls[i]:
				meme = {
					'imageUrl': urls[i],
					'text0': None,
					'text1': None,
					'datePosted': dates[i],
					'datePulled': time.time(),
					'source': 'reddit',
					'filename': '{}.png'.format(dates[i])
					
				}
		payload.get('memes').append(meme)
	
	with open(args.payloadFile, 'w') as f:
		f.write(json.dumps(payload))

def getImagesFromSubreddit(subreddit, args):
	urls = []
	dates = []
	
	for submission in subreddit.hot(limit=int(args.urlNumber)):
		#sleep for 1s so that we don't request too fast and violate reddit ToS
		time.sleep(1)

		url = submission.url
		# Ignored URLs
		if 'youtube' in url:
			continue

		# Fetch Images
		print(url)
		'''if '.jpg' in url:
			request.urlretrieve(url, '{}/image{}.jpg'.format(args.saveDirectory,i))
		elif '.png' in url:
			request.urlretrieve(url, '{}/image{}.png'.format(args.saveDirectory,i))'''
		if '.jpg' in url or '.png' in url:
			urls.append(url)
			dates.append(submission.created)
			
	return (urls, dates)

def getRandomSubreddit(subreddits):
	randomSubs = reddit.subreddits.search_by_topic('memes')
	randomSub = random.choice(randomSubs)
	
	while 'memes' not in randomSub.display_name and randomSub in subreddits:
		randomSub = random.choice(randomSubs)
		
		if 'memes' in randomSub.display_name or 'meme' in randomSub.display_name:
			break
	
	print(randomSub.display_name)
	return randomSub