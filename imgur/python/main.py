import argparse
from imgurpython import ImgurClient
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

def getMemeLinks():
    memes = []

    # Gather top memes for the week
    items = client.gallery_search("memes", sort='top', window= 'week')
    for item in items:
        memes.append(item)

    # Show top 5 memes
    memes = memes[:5]
    for meme in memes:
        print(meme.link)

    return memes

if __name__ == "__main__":
	pass

getMemeLinks()