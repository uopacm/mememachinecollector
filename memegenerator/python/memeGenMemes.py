import subprocess
import json
import pdb
import sys

def getMemes(args):
	p = None
	
	if sys.platform.startswith('win'):
		if args.popularNew:
			p = subprocess.Popen(['memegenerator/haskell/memgenerator-scraper.exe', '--channel', 'popular', '--outputFile', '{}_memegenerator.json'.format(args.payloadFile.replace('.json', ''))])
		else:
			p = subprocess.Popen(['memegenerator/haskell/memgenerator-scraper.exe', '--channel', 'new', '--outputFile', '{}_memegenerator.json'.format(args.payloadFile.replace('.json', ''))])
	elif sys.platform.startswith('linux'):
		if args.popularNew:
			# Put run code here
			print('Linux code to be implemented later...')
		else:
			# Put run code here
			print('Linux code to be implemented later...')
	elif sys.platform.startswith('darwin'):
		if args.popularNew:
			# Put run code here
			print('Mac OSX code to be implemented later...')
		else:
			# Put run code here
			print('Mac OSX code to be implemented later...')
	
	stdout, stderr = p.communicate()
	
	if stdout != None:
		print(stdout)
	
	if stderr != None:
		print(stderr)
	
	memeGenJSON = ''
	
	with open('{}_memegenerator.json'.format(args.payloadFile.replace('.json', '')), 'r') as f:
		for line in f:
			memeGenJSON += line
	
	memeGenList = memeGenJSON.split('}')
	memeText = ''
	
	for meme in range(len(memeGenList)):
		if meme != len(memeGenList) - 1:
			memeText += memeGenList[meme]
			memeText += ',"source":"memegenerator"},'
		elif meme == len(memeGenList):
			memeText += memeGenList[meme]
			memeText += '}'
		else:
			memeText += memeGenList[meme]
			memeText += '}'
	
	memeGenJSON = '{"memes":[' + memeText + ']}'
	memeGenJSON = memeGenJSON.replace('},}]}', '}]}')
	
	currentPayload = ''
	
	with open(args.payloadFile, 'r') as f:
		for line in f:
			currentPayload += line
	
	payloadDict = json.loads(currentPayload)
	pdb.set_trace()
	memeGenDict = json.loads(memeGenJSON)
	
	for meme in memeGenDict.get('memes'):
		payloadDict.get('memes').append(meme)
		payloadDict.setdefault('source', 'memegenerator')
	
	with open(args.payloadFile, 'w') as f:
		f.write(json.dumps(payloadDict))