# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:54:59 2015

@author: LUISFELIPE
"""

import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://trenesytiempos.blogspot.com.es/'
html = urllib.request.urlopen(url).read()
sopa = BeautifulSoup(html, "html.parser")

#getting all the 2015 registers
enlaces =sopa.find_all(href=re.compile("/2015"),class_="post-count-link")

#filling the array with its values
enlaceList = []
for enlace in enlaces:
    enlaceList.append(enlace['href'])

imgListTemp = []
           
"""for enlace in enlaceList:
    html = urllib.request.urlopen(enlace).read()
    sopa = BeautifulSoup(html, "html.parser")
    img = sopa.find_all('img', {"border":"0"})
    for imgUrl in img:
        imgListTemp.append(imgUrl['src'])"""