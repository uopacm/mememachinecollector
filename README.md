# Meme Machine
This repository is for the UOP ACM Meme Machine. Its intended purpose will be to gather, rate, and create memes. We are currently focused on the gathering section of the meme machine.

This repository is divided into folders based on the language the code is written in. If you know Haskell, feel free to edit the code contained in the haskell folder or write more for haskell because why not. If you would like to write a portion of the Meme Machine in another programming language, create a new folder for it.

### Haskell
Currently, this folder only contains code for downloading memes from memegenerator.net. If anyone knows Haskell and would like to contribute to this portion of the repo, feel free to add.

### Python
This is the main portion of our code for the Meme Machine. I'll explain each of the parts here.

##### Memegenerator
This part of the repository simply grabs a json payload from the website's api address and adds it to the overall payload json file. Currently, the images downloaded from memegenerator.net do not have the text in the picture; it's only included in the json payload. I (skeetcha/Daniel) have attempted to try to categorize them, but from what I remember, I didn't have much progress.

##### Reddit
This requires the *praw* library. It uses the *subredditsList.txt* file to look at specific subreddits, as well as one other random subreddit that has the word *meme* in the display_name attribute.

##### Imgur
This requires the *imgurpython* library. This grabs all images from galleries labeled *memes* (note to the team, please add an argument for this, it will get very crowded in our folder if we allow all pictures to be downloaded from *multiple* galleries).

##### Tumblr
Needs to be written.

##### main.py
This file holds the code that downloads each of the pictures that are put into the collated json payload file.

|Argument|Module|Description|
|:-:|:-:|:-:|
|urlNumber|Reddit|The amount of urls/pictures to download from each subreddit|
|subReddits|Reddit|The subredditList.txt file to pull from|
|saveDirectory|Downloader|The directory that will store the downloaded memes|
|popularNew|Memegenerator|Whether or not to grab Popular or New memes from memegenerator.net|
|payloadFile|All|The name of the collated json payload file|

Updated February 8th, 2018 by skeetcha (Daniel)