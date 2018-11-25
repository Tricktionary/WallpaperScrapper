import sys
import requests 

URL = 'https://www.reddit.com/r/iWallpaper.json'

response = requests.get(url = URL)

dataResponse = response.json()
print(dataResponse)
dataList = dataResponse['data']['children']


sys.stdout = open('urlData.txt','w')
for data in dataList:
    print(data['data']['url'] )


