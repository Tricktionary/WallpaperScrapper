# WallpaperScraper

### Purpose 
A script used for scrapping all the wallpaper hyper links from Reddit 

### How to run

- Have Python3 installed 
- run `source venv/bin/activate`

#### htmlScraper.py
Is a beautifulsoup attempt of scrapping information off of reddit. It works but 
reddit does not give reddit links in the DOM. In order to achive this we would need 
to scrape via a headless browser. (Deprecated)

`python3 htmlScraper.py`

#### jsonScraper.py
Reddit supplies user with the data value if you tag `.json` on the end of the url
so I added this and parsed the response for all image related links and downloaded them to an
`/image` directory. (Need to paginate)

`python3 jsonScraper.py`