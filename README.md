# UTC503 / @public_museum

## PROJECT AIM :

Publish artworks on @public_museum Twitter account.

## HOW TO ?

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

Run images_request.py :
```
$ python3 images_request.py
```
Once images are downloaded run twitter.py :
```
$ python3 twitter.py
```

### RUN FIRST images_request.py.

> image_request.py download images & description from https://www.artmajeur.com/fr/oeuvres-d-art/sculpture/bronze-1432 in the file directory.


### RUN SECONDLY tweeter.py

> tweeter.py publish on @public_museum Twitter account the previously downloaded images.
