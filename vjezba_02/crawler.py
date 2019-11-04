from bs4 import BeautifulSoup
import requests

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
        link = anchor.get("href")
        if link is not None and link.startswith("http") and link not in links:
            links.append(link)

print(links)
