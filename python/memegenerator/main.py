import requests
import json
import time

popularUrl = 'http://version1.api.memegenerator.net/Instances_Select_ByPopular'
newUrl = 'http://version1.api.memegenerator.net/Instances_Select_ByNew'

def getMemes(args):
	popularReq = requests.get(url=popularUrl)
	newReq = requests.get(url=newUrl)
	popularDict = popularReq.json()
	newDict = newReq.json()
	payload = {
		'memes': []
	}
	
	if args.popularNew:
		if popularDict.get('success'):
			for i in range(args.urlNumber):
				print(popularDict.get('result')[i].get('imageUrl'))
				meme = {
					'url': popularDict.get('result')[i].get('imageUrl'),
					'text0': popularDict.get('result')[i].get('text0'),
					'text1': popularDict.get('result')[i].get('text1'),
					'datePosted': None,
					'datePulled': int(time.time()),
					'source': 'memegenerator',
					'title': popularDict.get('result')[i].get('title'),
					'filename': i
				}
				payload.get('memes').append(meme)
			
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
		else:
			print('Pull not successful!')
	else:
		if newDict.get('success'):
			for i in range(args.urlNumber):
				print(newDict.get('result')[i].get('imageUrl'))
				meme = {
					'url': newDict.get('result')[i].get('imageUrl'),
					'text0': newDict.get('result')[i].get('text0'),
					'text1': newDict.get('result')[i].get('text1'),
					'datePosted': None,
					'datePulled': int(time.time()),
					'source': 'memegenerator',
					'filename': i
				}
				payload.get('memes').append(meme)
			
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