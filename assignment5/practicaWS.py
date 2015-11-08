# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:54:59 2015

@author: LUISFELIPE
"""

import urllib.request
from bs4 import BeautifulSoup
import re
import os

url = 'http://trenesytiempos.blogspot.com.es/'
html = urllib.request.urlopen(url).read()
sopa = BeautifulSoup(html, "html.parser")

#getting all the 2015 registers
enlaces =sopa.find_all(href=re.compile("/2015"),class_="post-count-link")

#filling the array with its values
dirList = []
enlaceList = []

for enlace in enlaces:
    path = (enlace.text).strip()
    enlaceList.append(enlace['href'])
    #dirList.append(os.path.join(path)) 
    # Python breaks '/' character, so it's creating a lot of directories

#Creating so many Directories... ERROR     
#for directory in dirList:
#    os.makedirs(directory)
    
imgListTemp = []

#filling imgList with all the images of each link in enlaceList           
for enlace in enlaceList:
    img = urllib.request.urlopen(enlace).read()
    sopa = BeautifulSoup(img, "html.parser")
    all_images = sopa.find_all("img", border="0")
    for imgs in all_images:
        imgListTemp.append(imgs['src'])