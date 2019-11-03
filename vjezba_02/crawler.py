'''
import requests
import re

res = requests.get('https://www.sheldonbrown.com')
##body = re.findall('(?s)<body>(.*)<\/body>', res.text)[0]
links = re.findall('<a\s+(?:[^>]*?\s+)?href=(["\'])(.*?)\1', res.text)

print(links)
'''

from bs4 import BeautifulSoup
import requests
import re

linksVisited = 0

links = ["https://www.sheldonbrown.com/"]
linksIndex = 0

while linksVisited < 50:
    pageValid = False

    while not pageValid:
        url = links[linksIndex]
        page = requests.get(url)
        linksIndex += 1

        if page.status_code == 200:
            pageValid = True
            linksVisited += 1

    data = page.text
    soup = BeautifulSoup(data, "html.parser")

    for anchor in soup.find_all('a'):
        link = anchor.get('href')
        if link is not None and re.search("http.*", link) and link not in links:
            links.append(link)

print(links)
