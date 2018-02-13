import urllib.request
import requests, os, re, sys
from bs4 import BeautifulSoup

erro = 0
def Comic(imageUrl):
    erro = 0
    page = requests.get(imageUrl).content
    soup = BeautifulSoup(page,"html.parser")
    comicImageBlock = soup.find("div",{"id":"comic"})
    comicImageTag = comicImageBlock.find("img")
    comicURL = comicImageTag['src']
    m = re.search(r"[\w_()]+\.[jppng]*$", comicURL)
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.isfile('images/{}'.format(m.group(0))):
        urllib.request.urlretrieve("http:{}".format(comicURL), "images/"+m.group(0))
        print("Downloaded:\t{0}".format(m.group(0)))


for i in range(1940,sys.maxsize):
    try:
        Comic("https://xkcd.com/{0}".format(i))
    except:
        erro = erro +1
        if(erro > 3):
            print("Finished")
            break
