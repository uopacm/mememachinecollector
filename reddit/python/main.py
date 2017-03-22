import argparse
import praw
import os
import time
from urllib import request
import random

parser = argparse.ArgumentParser(description='Fetch URLs of reddit images')
parser.add_argument('urlNumber', type=int, help='Number of URLs to look up per subreddit')
parser.add_argument('saveDirectory', type=str, help='Directory to save images in')
parser.add_argument('subReddits', type=str, help='File containing list of subreddits', default="subredditList.txt")
args = parser.parse_args()

reddit = praw.Reddit(client_id='B8ZEg7a304hCfw',
	client_secret='wWoLUJrIAWGbPddy3W0lzU7dVqw',
	user_agent='meme-machine:reddit-collector:v1.0 (by /u/theMusicalGamer88)')

def main():
	subredditsFile = open(args.subReddits, "r")

	subreddits = []

	#read subreddit names from file into list "subreddits" as subreddit objects
	for line in subredditsFile.readlines():
		subreddits.append(reddit.subreddit(line.strip()))

	#for every subreddit, get Images
	for subreddit in subreddits:
		getImagesFromSubreddit(subreddit)
	
	subreddit = getRandomSubreddit(subreddits)
	getImagesFromSubreddit(subreddit)

def getImagesFromSubreddit(subreddit):
	for i,submission in enumerate(subreddit.hot(limit=int(args.urlNumber))):
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
		if '.jpg' in url:
			request.urlretrieve(url, '{}/{}.jpg'.format(args.saveDirectory,submission.id))
		elif '.png' in url:
			request.urlretrieve(url, '{}/{}.png'.format(args.saveDirectory,submission.id))

def getRandomSubreddit(subreddits):
	randomSubs = reddit.subreddits.search_by_topic('memes')
	randomSub = random.choice(randomSubs)
	
	while 'memes' not in randomSub.display_name and randomSub in subreddits:
		randomSub = random.choice(randomSubs)
		
		if 'memes' in randomSub.display_name or 'meme' in randomSub.display_name:
			break
	
	print(randomSub.display_name)
	return randomSub

if __name__ == "__main__":
	# Create the requested directory if it does not exist
	if not os.path.exists(args.saveDirectory):
		os.makedirs(args.saveDirectory)

	main()
