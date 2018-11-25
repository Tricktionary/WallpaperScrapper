import sys
import urllib.request as urllib2 
from bs4 import BeautifulSoup
 

wiki = "https://www.reddit.com/r/iWallpaper/"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,"html.parser")

#Open a txt file and writes data to it 
sys.stdout = open('PageUrl.txt','w')

for link in soup.findAll('a'):
    print(link.get('href'))