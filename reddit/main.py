import argparse
import praw
import os
import time
from urllib import request

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

	#TODO:Fix this garbage code
	#i forgot how to make an empty list in python, then append objects to it, so i did this for now :(
	#austin pls halp
	subreddits = [reddit.subreddit("nice_meme")];
	subreddits.pop(0)

	#read subreddit names from file into list "subreddits" as subreddit objects
	for line in subredditsFile.readlines():
		subreddits.append(reddit.subreddit(line.strip()))

	#for every subreddit, get Images
	for subreddit in subreddits:
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
		if '.jpg' in url:
			request.urlretrieve(url, '{}/image{}.jpg'.format(args.saveDirectory,i))
		elif '.png' in url:
				request.urlretrieve(url, '{}/image{}.png'.format(args.saveDirectory,i))

if __name__ == "__main__":
	# Create the requested directory if it does not exist
	if not os.path.exists(args.saveDirectory):
		os.makedirs(args.saveDirectory)

	main()
