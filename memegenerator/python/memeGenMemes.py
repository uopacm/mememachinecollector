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
					'text0': popularDict.get('result')[i].get('imageID'),
					'datePulled': int(time.time()),
					'source': 'memegenerator'
				}
				payload.get('memes').append(meme)
			
			return json.dumps(payload, ensure_ascii=False) # I will test this soon, and if I don't, please do. If this part crashes, change ensure_ascii to True.
		else:
			print('Pull not successful!')
	else:
		if newDict.get('success'):
			for i in range(args.urlNumber):
				print(newDict.get('result')[i].get('imageUrl'))
				meme = {
					'url': newDict.get('result')[i].get('imageUrl'),
					'text0': newDict.get('result')[i].get('imageID'),
					'datePulled': int(time.time()),
					'source': 'memegenerator'
				}
				payload.get('memes').append(meme)
			
			return json.dumps(payload, ensure_ascii=False) # same as above