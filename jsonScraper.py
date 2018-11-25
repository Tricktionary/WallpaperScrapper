import sys
import os
import requests 
import urllib
import urllib.request as req


URL = 'https://www.reddit.com/r/iWallpaper/.json?limit=100&after=t3_10omtd/'

response = requests.get(url = URL)

imgUrls = []
jsonResponse = response.json()
dataObj = jsonResponse['data']['children']

os.mkdir('image')
sys.stdout = open('urlData.txt','w')
for data in dataObj:
    if 'https://www.reddit.com/r/iWallpaper/comments/' not in data['data']['url']:
        print(data['data']['url'] )
        imgUrls.append(data['data']['url'])


for i in range(0,len(imgUrls)):
        req.urlretrieve(imgUrls[i], "image/wallpaper_"+str(i)+".jpg")


