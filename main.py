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
parser.add_argument('payloadFile', type=str, help='File name of the json file', default='payload.json')
args = parser.parse_args()

def main():
	# Receive from Reddit
	print('Receiving JSON payload from Reddit...')
	redditMemes.getMemes(args)
	
	# Receive from Imgur
	print('Receiving JSON payload from Imgur...')
	imgurMemes.getMemes(args)
	
	# Receive from MemeGenerator
	print('Receiving JSON payload from MemeGenerator...')
	memeGenMemes.getMemes(args)
	
	# Parse JSON file
	print('Parsing JSON file {}...'.format(args.payloadFile))
	payload = {}
	with open(args.payloadFile, 'r') as f:
		jsonString = ''
		for line in f:
			jsonString += line
		payload = json.loads(jsonString)
	
	download(payload.get('memes'))

def download(memeList):
	for meme in memeList:
		time.sleep(1)
		print('Downloading ' + meme.get('url') + '...')
		
		if '.jpg' in meme.get('url'):
			request.urlretrieve(meme.get('url'), '{}/{}{}.jpg'.format(args.saveDirectory, meme.get('source'), meme.get('text0')))
		elif '.png' in meme.get('url'):
			request.urlretrieve(meme.get('url'), '{}/{}{}.png'.format(args.saveDirectory, meme.get('source'), meme.get('text0')))
		
		print('Done.')

if __name__ == '__main__':
	if not os.path.exists(args.saveDirectory):
		os.makedirs(args.saveDirectory)
	
	if not os.path.exists(args.payloadFile):
		with open(args.payloadFile, 'w') as f:
			f.close()
	
	main()