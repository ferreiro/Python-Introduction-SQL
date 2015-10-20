# -*- coding: utf-8 -*-
import xml
import urllib
import xml.etree.ElementTree

googleXML_API = "http://maps.googleapis.com/maps/api/geocode/xml?"

# http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python

def callAPI(address, sensor):
	global googleXML_API

	# parameters = "address=" + address + "&sensor=" + sensor 
	parameters = urllib.urlencode({'address': address, 'sensor':'false'});
	url  = googleXML_API + parameters

	print "Calling " + url

	uh 	 = urllib.urlopen(url)
	data = uh.read();

	# print "Recuperados", len(data), 'characters'

	e = xml.etree.ElementTree.parse(data).getroot()

	for atype in e.findall('address'):
		print atype
	    #print(atype.get('address'))


callAPI('madrid', 'false');