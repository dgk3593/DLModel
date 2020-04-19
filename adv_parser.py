# Get data from Gamepedia Grid

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import requests

url = "https://dragalialost.gamepedia.com/Adventurer_Grid"
html = requests.get(url).text
soup = BeautifulSoup(html, features="html.parser")
advs = soup.find_all(class_="character-grid-entry grid-entry")

adv_dict = {}

for adv in advs:

    tmpdict = {}    #temporary dict

    tmpdict['element'] = adv['data-element']
    tmpdict['rarity'] = adv['data-rarity']
    tmpdict['class'] = adv['data-class']
    tmpdict['weapon'] = adv['data-weapon']
    # Get name
    temp = adv.select(".character-grid-entry-title")
    title = temp[0].find('a')['title']
    tmpdict['name'] = title.replace('\'s','') # remove '

    # Get title
    temp = adv.select(".character-grid-entry-subtitle")
    temp = temp[0].contents
    subtitle = temp[0]
    tmpdict['title'] = subtitle

    # Look for image link
    temp = adv.find_all('img')
    temp = temp[1]['srcset']    # str contains 2 links

    start = False
    link = ''
    for c in temp:
        if start == True:
            link = link + c
        else:
            if c == ' ':
                start = True
    link = link[6:-3]
    tmpdict['imglink'] =link

    # Find id
    s = link.find('r05')
    if link[s-3] != '0':
        id = link[s-11:s-1]
    else:
        id = link[s-10:s-1]
    adv_dict[id] = tmpdict

    # download 300 x 300 images
    # dest = "images/full_body/" + id + ".png"
    # with open(dest, 'wb') as handle:
    #     response = requests.get(link, stream=True)
    #
    #     if not response.ok:
    #         print(response)
    #
    #     for block in response.iter_content(1024):
    #         if not block:
    #             break
    #
    #         handle.write(block)


f = open('adv_dict.txt','w')
f.write(str(adv_dict))
f.close()
