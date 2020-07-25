import ctypes
import urllib.request
import time
import os, sys
from bs4 import BeautifulSoup
try:
    print("Setting wallpaper!")
    url = "https://apod.nasa.gov/apod/astropix.html"
    page = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    for image in page.findAll("img"):
        print("Image: %(src)s" % image)
        #pass
    parsed = "http://apod.nasa.gov/apod/"+"%(src)s" % image
    x = urllib.request.urlretrieve(parsed)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, x[0], 3)
    os.remove(x[0])
    sys.exit(0)
    #time.sleep(86400)
except:
    print('error')
    sys.exit(1)
