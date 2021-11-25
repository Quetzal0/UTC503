import urllib.request

with urllib.request.urlopen('https://www.reddit.com/r/museum/top/') as response:
    html = response.read()
    print(html)