# Necessary imports
import urllib.request
import requests, os, re, sys
from bs4 import BeautifulSoup

erro = 0    # Global variable to count errors

# function which will download image though URL
def Comic(imageUrl):
    erro = 0    # Sets to Zero if there isn't continous errors
    page = requests.get(imageUrl).content   # stores the content from the requested url in page
    soup = BeautifulSoup(page,"html.parser")    # Runs the BeautifulSoup parsing package
    comicImageBlock = soup.find("div",{"id":"comic"})   # finds the image block and stores in comicImageBlock
    comicImageTag = comicImageBlock.find("img")         # finds the image tag and stores in comicImageTag
    comicURL = comicImageTag['src']                     # Stores the src of ImageTag in comicURL
    m = re.search(r"[\w_()]+\.[jppng]*$", comicURL)     # Finds the image name from URL and stores in m as group
    if not os.path.exists('images'):                    # Check whether image directory is present if not then
        os.makedirs('images')                           # Creates a directory named images
    if not os.path.isfile('images/{}'.format(m.group(0))): # Check whether target image is present if not then
        urllib.request.urlretrieve("http:{}".format(comicURL), "images/"+m.group(0))    # Downloads from the url and saves
        print("Downloaded:\t{0}".format(m.group(0)))    # Print the filename which is downloaded on console


for i in range(1,sys.maxsize):      # For looping all the possible numbers
    try:                            
        Comic("https://xkcd.com/{0}".format(i))     # Passes URL of all the possible 
    except:
        erro = erro +1      # If any error occurs errors incremented
        if(erro > 3):       # If error occurs continously 3 times that means there isn't any more pages
            print("Finished")   # Now we can display it is finished
            break               # Break the loop and terminate the program
