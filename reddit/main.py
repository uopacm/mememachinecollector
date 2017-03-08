import argparse
import praw

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('arg1', help='1st Argument')
args = parser.parse_args()
reddit = praw.Reddit(client_id='B8ZEg7a304hCfw',
	client_secret='wWoLUJrIAWGbPddy3W0lzU7dVqw',
	user_agent='meme-machine:reddit-collector:v1.0 (by /u/theMusicalGamer88)')

if __name__ == "__main__":
	pass 
