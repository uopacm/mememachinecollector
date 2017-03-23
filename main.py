from reddit.python import redditMemes
from imgur.python import imgurMemes
import json
from urllib import request

parser = argparse.ArgumentParser(description='Save memes in a directory')
parser.add_argument('saveDirectory', type=str, help='Directory to save images in')
args = parser.parse_args()

def main():
	# Receive from Reddit
	reddit = redditMemes.getMemes()
	redditJson = json.loads(reddit)
	download(redditJson.get('memes'))
	
	# Receive from Imgur
	imgur = imgurMemes.getMemes()
	imgurJson = json.loads(imgur)
	download(imgurJson.get('memes'))

def download(memeList):
	for meme in memeList:
		print('Downloading ' + meme.get('url') + '...')
		
		if '.jpg' in url:
			request.urlretrieve(url, '{}/{}.jpg'.format(args.saveDirectory, meme.get('text0')))
		elif '.png' in url:
			request.urlretrieve(url, '{}/{}.png'.format(args.saveDirectory, meme.get('text0')))

if __name__ == '__main__':
	main()