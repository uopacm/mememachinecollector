from reddit.python import redditMemes
from imgur.python import imgurMemes
import json
from urllib import request
import time
import argparse
import os

parser = argparse.ArgumentParser(description='Save memes in a directory')
parser.add_argument('urlNumber', type=int, help='Number of URLs to look up per subreddit')
parser.add_argument('subReddits', type=str, help='File containing list of subreddits', default="subredditList.txt")
parser.add_argument('saveDirectory', type=str, help='Directory to save images in')
args = parser.parse_args()

def main():
	memeDict = {
		'memes': []
	}
	# Receive from Reddit
	reddit = redditMemes.getMemes(args)
	redditJson = json.loads(reddit)
	for meme in redditJson.get('memes'):
		memeDict.get('memes').append(meme)
	
	# Receive from Imgur
	imgur = imgurMemes.getMemes()
	imgurJson = json.loads(imgur)
	for meme in imgurJson.get('memes'):
		memeDict.get('memes').append(meme)
	
	download(memeDict.get('memes'))

def download(memeList):
	for meme in memeList:
		time.sleep(1)
		print('Downloading ' + meme.get('url') + '...')
		
		if '.jpg' in meme.get('url'):
			request.urlretrieve(meme.get('url'), '{}/{}.jpg'.format(args.saveDirectory, meme.get('text0')))
		elif '.png' in meme.get('url'):
			request.urlretrieve(meme.get('url'), '{}/{}.png'.format(args.saveDirectory, meme.get('text0')))

if __name__ == '__main__':
	if not os.path.exists(args.saveDirectory):
		os.makedirs(args.saveDirectory)
	
	main()