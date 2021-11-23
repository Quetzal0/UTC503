import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.reddit.com/r/museum/top/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all("img", attrs = {"class": "_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax"})

number = 0

print(images)

for image in images:
	image_src = image["src"]
	print(image_src)
	urllib.request.urlretrieve(image_src, str(number))
	number += 1