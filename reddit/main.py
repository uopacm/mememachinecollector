import argparse
import praw
from urllib import request

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('urlNumber', help='Number of URLs to look up')
args = parser.parse_args()

reddit = praw.Reddit(client_id='B8ZEg7a304hCfw',
	client_secret='wWoLUJrIAWGbPddy3W0lzU7dVqw',
	user_agent='meme-machine:reddit-collector:v1.0 (by /u/theMusicalGamer88)')

def main():
	subreddit = reddit.subreddit('startrekmemes')
	tenurls = []
	for i,submission in enumerate(subreddit.hot(limit=int(args.urlNumber))):
		if 'youtube' not in submission.url:
			tenurls.append(submission.url)

	for i,url in enumerate(tenurls):
		print(url)

		if '.jpg' in url:
			request.urlretrieve(url, 'image.' + str(i) + '.jpg')
		elif '.png' in url:
				request.urlretrieve(url, 'image.' + str(i) + '.png')

if __name__ == "__main__":
	main()
