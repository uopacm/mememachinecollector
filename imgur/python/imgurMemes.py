import argparse
from imgurpython import ImgurClient
import time
import json
import pdb
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

def getMemes(args):
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
		
		for i in range(args.urlNumber):
			if i >= len(album):
				i = len(album) - 1
			images.append(album[i])
	
	for image in images:
		ids.append(image.id)
	
	payload = {
		'memes': []
	}
	
	for i,id in enumerate(ids):
		print('http://imgur.com/{}.png'.format(id))
		pMeme = {
			'url': 'http://imgur.com/{}.png'.format(id),
			'text0': i,
			'datePulled': int(time.time()),
			'source': 'imgur'
		}
		payload.get('memes').append(pMeme)
	
	currentPayload = {}
	with open(args.payloadFile, 'r') as f:
		jsonString = ''
		for line in f:
			jsonString += line
			jsonString += '\n'
		currentPayload = json.loads(jsonString)
	
	for meme in payload.get('memes'):
		currentPayload.get('memes').append(meme)
	
	with open(args.payloadFile, 'w') as f:
		f.write(json.dumps(currentPayload))