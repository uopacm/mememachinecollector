import argparse
from imgurpython import ImgurClient
import time
import json
# Install:
# python -m pip install imgurpython

"""
Errors out
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('arg1', help='1st Argument')
args = parser.parse_args()
"""

# User: PacificACM
client_id = '8597f0ab26ae048'
client_secret = '6ac86735ce1cc66ba6509ba6224446eb17554dc9'

client = ImgurClient(client_id, client_secret)

def getMemes():
	memes = []
	ids = []
	
	# Gather top memes for the week
	items = client.gallery_search("memes", sort='top', window= 'week')
	for item in items:
		memes.append(item)
	
	# Show top 5 memes
	memes = memes[:5]
	images = []
	for meme in memes:
		album = client.get_album_images(meme.link[19:])
		
		for i in album:
			images.append(i)
	
	for image in images:
		ids.append(image.id)
	
	payload = {
		'memes': []
	}
	
	for id in ids:
		pMeme = {
			'url': 'http://imgur.com/{}.png'.format(id),
			'text0': id,
			'datePosted': 0, # Not entirely sure how the ImgurClient works, and also can't look it up at this time (no WiFi in Tahoe)
			'datePulled': int(time.time())
		}
		payload.get('memes').append(pMeme)
	
	return json.dumps(payload, ensure_ascii=False) # If this gives you an error, change ensure_ascii to True