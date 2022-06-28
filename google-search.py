import urllib
import requests
from bs4 import BeautifulSoup
import sys, math

if len(sys.argv) != 3:
        print("Usage:   ", sys.argv[0], "  {Search Query}                     {Count}")
        print("Example: ", sys.argv[0], '  "site:microsoft.com filetype:pdf"   50')
        exit()

query = sys.argv[1]
query = query.replace(' ', '+')
count = sys.argv[2]

headers = {
'Host': 'www.google.com',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'close',
'Upgrade-Insecure-Requests': '1'
}

start = 0
counter = int(math.ceil(int(count)/50.0)) * 50

for i in range(0, counter, 50):
	print("###############################################################################################################")
	print("Search results from", i, "to", i+50)
	print("###############################################################################################################")
	URL = "https://google.com/search?q="+query+"&num=50&start="+str(start)

	resp = requests.get(URL, headers=headers)
	print(resp)

	if resp.status_code == 200:
		soup = BeautifulSoup(resp.content, "html.parser")
		results = []
		for g in soup.find_all('div', class_='r'):
		    anchors = g.find_all('a')
		    if anchors:
		        link = anchors[0]['href']
		        title = g.find('h3').text
		        item = {
		            "title": title,
		            "link": link
		        }
		        results.append(item)
		        print("Title:", title)
		        print("Link:", link)
		        print("")
