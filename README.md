# UTC503 / @public_museum

## PROJECT AIM :

Publish artworks on @public_museum Twitter account.

## HOW TO ?

> - To use this script you must create a Twitter developper account.
> - Create your python project in the Twitter developper portal.
> - https://developer.twitter.com/en/portal/dashboard

Clone this repository to your device with the following command :
```
$ git clone https://github.com/Quetzal0/UTC503/
```
Then, run the following commands :
```
$ cd UTC503
$ ls
```
You can see this content :
- Code
- References
- README.md
- requirements.txt

Enter in the Code/ folder :
```
$ cd Code
```
Show the content :
```
$ ls
```
You can see this :
- config.py
- images_request_linux.py
- images_request_win.py
- twitter_linux.py
- twitter_win.py

> - Store your Twitter developper project creds in the config.py file.
> - images_request.py is the module that download all images that we need.
> - twitter.py is the main file, run it to punlish an image on your Twitter account.

#### Last step : 
> Edit file paths in images_request.py and twitter.py script. Just replace 'your path here' by your real path to the project folder.

### Then ;

run script for your system :
> twitter_win.py for Windows systems
```
$ python3 twitter_win.py
```
## When all done :

Create a scheduled task to automatically run the Twitter.py script.

## Enjoy !


## Known issues

This script as been writed on a Microsoft Windows device. Windows use a different way than Linux or MacOS for file paths. So be careful to paths if you don't use Windows.

