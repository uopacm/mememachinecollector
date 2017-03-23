from reddit.python import redditMemes
import json
from urllib import request

def main():
	# Receive from Reddit
	reddit = redditMemes.getMemes()
	redditJson = json.loads(reddit)
	
	for meme in redditJson.get('memes'):
		print('Downloading ' + meme.get('url') + '...')
		
		if '.jpg' in url:
			request.urlretrieve(url, '{}/{}.jpg'.format(redditMemes.args.saveDirectory, meme.get('text0')))
		elif '.png' in url:
			request.urlretrieve(url, '{}/{}.png'.format(redditMemes.args.saveDirectory, meme.get('text0')))
		
		print('Done.')

if __name__ == '__main__':
	main()