# Get data from Gamepedia Grid

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import requests

url = "https://dragalialost.gamepedia.com/Adventurer_List"
html = requests.get(url).text
soup = BeautifulSoup(html, features="html.parser")
advs = soup.find_all(class_="character-grid-entry grid-entry")

counter = 0

for adv in advs:

    items = adv.find_all("td")
    temp = items[0]
    temp = temp.find("img")
    link = temp['src']
    file_name = temp['alt'].replace(' ', '_')

    # download icons
    dest = "images/icon/" + file_name
    with open(dest, 'wb') as handle:
        response = requests.get(link, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
