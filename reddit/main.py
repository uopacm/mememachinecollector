import argparse
import praw
import os
from urllib import request

parser = argparse.ArgumentParser(description='Fetch URLs of reddit images')
parser.add_argument('urlNumber', type=int, help='Number of URLs to look up')
parser.add_argument('saveDirectory', type=str, help='Directory to save images in')
parser.add_argument('subreddit', type=str, help='Requested subreddit', default="startrekmemes")
args = parser.parse_args()

reddit = praw.Reddit(client_id='B8ZEg7a304hCfw',
	client_secret='wWoLUJrIAWGbPddy3W0lzU7dVqw',
	user_agent='meme-machine:reddit-collector:v1.0 (by /u/theMusicalGamer88)')

def main():
	subreddit = reddit.subreddit(args.subreddit)
	for i,submission in enumerate(subreddit.hot(limit=int(args.urlNumber))):
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
