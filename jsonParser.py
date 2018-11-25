import sys
import requests 

URL = 'https://www.reddit.com/r/iWallpaper/.json?count=100&after=t3_10omtd/'

response = requests.get(url = URL)

dataResponse = response.json()
#print(dataResponse)
dataList = dataResponse['data']['children']


sys.stdout = open('urlData.txt','w')
for data in dataList:
    if 'https://www.reddit.com/r/iWallpaper/comments/' not in data['data']['url']:
        print(data['data']['url'] )


