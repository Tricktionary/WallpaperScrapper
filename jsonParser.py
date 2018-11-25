import sys
import requests 

URL = 'https://www.reddit.com/r/iWallpaper.json'

response = requests.get(url = URL)

data = response.json()
sys.stdout = open('urlData.txt','w')
print(data)
