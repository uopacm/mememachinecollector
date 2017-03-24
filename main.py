from reddit.python import redditMemes
from imgur.python import imgurMemes
from memegenerator.python import memeGenMemes
import json
from urllib import request
import time
import argparse
import os

parser = argparse.ArgumentParser(description='Save memes in a directory')
parser.add_argument('urlNumber', type=int, help='Number of URLs to look up per subreddit')
parser.add_argument('subReddits', type=str, help='File containing list of subreddits', default="subredditList.txt")
parser.add_argument('saveDirectory', type=str, help='Directory to save images in')
parser.add_argument('popularNew', type=bool, help='Get Popular (1) or New (0) Memes from MemeGenerator', default=False)
args = parser.parse_args()

def main():
	memeDict = {
		'memes': []
	}
	# Receive from Reddit
	print('Receiving JSON payload from Reddit...')
	reddit = redditMemes.getMemes(args)
	redditJson = json.loads(reddit)
	for meme in redditJson.get('memes'):
		memeDict.get('memes').append(meme)
	
	# Receive from Imgur
	print('Receiving JSON payload from Imgur...')
	imgur = imgurMemes.getMemes(args)
	imgurJson = json.loads(imgur)
	for meme in imgurJson.get('memes'):
		memeDict.get('memes').append(meme)
	
	# Receive from MemeGenerator
	print('Receiving JSON payload from MemeGenerator...')
	memeGen = memeGenMemes.getMemes(args)
	memeGenJson = json.loads(memeGen)
	for meme in memeGenJson.get('memes'):
		memeDict.get('memes').append(meme)
	
	with open('payload.json', 'w') as f:
		f.write(json.dumps(memeDict, ensure_ascii=True))
	
	download(memeDict.get('memes'))

def download(memeList):
	for meme in memeList:
		time.sleep(1)
		print('Downloading ' + meme.get('url') + '...')
		
		if meme.get('source') == 'reddit':
			if '.jpg' in meme.get('url'):
				request.urlretrieve(meme.get('url'), '{}/{}{}.jpg'.format(args.saveDirectory, meme.get('source'), meme.get('text0')))
			elif '.png' in meme.get('url'):
				request.urlretrieve(meme.get('url'), '{}/{}{}.png'.format(args.saveDirectory, meme.get('source'), meme.get('text0')))
		
		print('Done.')

if __name__ == '__main__':
	if not os.path.exists(args.saveDirectory):
		os.makedirs(args.saveDirectory)
	
	main()