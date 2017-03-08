import argparse
import praw
from urllib import request

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('arg1', help='1st Argument')
args = parser.parse_args()
reddit = praw.Reddit(client_id='B8ZEg7a304hCfw',
	client_secret='wWoLUJrIAWGbPddy3W0lzU7dVqw',
	user_agent='meme-machine:reddit-collector:v1.0 (by /u/theMusicalGamer88)')

def main():
        subreddit = reddit.subreddit('startrekmemes')
        tenurls = []
        for submission in subreddit.hot(limit=10):
                if 'youtube' not in submission.url:
                        tenurls.append(submission.url)
        i = 0

        for url in tenurls:
                print(url)

                if '.jpg' in url:
                        request.urlretrieve(url, 'image.' + str(i) + '.jpg')
                elif '.png' in url:
                        request.urlretrieve(url, 'image.' + str(i) + '.png')
                
                i += 1

if __name__ == "__main__":
	main()
