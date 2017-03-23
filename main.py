from reddit.python import redditMemes
from imgur.python import imgurMemes
import json
from urllib import request
import time

parser = argparse.ArgumentParser(description='Save memes in a directory')
parser.add_argument('saveDirectory', type=str, help='Directory to save images in')
args = parser.parse_args()

def main():
	memeDict = {
		'memes': []
	}
	# Receive from Reddit
	reddit = redditMemes.getMemes()
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
		
		if '.jpg' in url:
			request.urlretrieve(url, '{}/{}.jpg'.format(args.saveDirectory, meme.get('text0')))
		elif '.png' in url:
			request.urlretrieve(url, '{}/{}.png'.format(args.saveDirectory, meme.get('text0')))

if __name__ == '__main__':
	main()