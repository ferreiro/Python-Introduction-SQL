# -*- coding: utf-8 -*-
import xml
import urllib
from xml.etree import ElementTree

outputFile 	  = "test.xml"
googleXML_API = "http://maps.googleapis.com/maps/api/geocode/xml?"

def readXML(data):
	tree  = ElementTree.fromstring(data)
	return tree

def checkValidTree(xmlTree):
	# Google api specific attribute
	if (xmlTree[0].tag == "status"): 
		if (xmlTree[0].text == "OK"):
			return 0
		else:
			return -1

def printInformation(data):
	print "| Information"
	print "Name: %s" % data['name']
	print "Country: %s" % data['country']
	print "Short name of Country: %s" % data['short_name']
	print "Level 1 entity: %s" % data['level_1_entity']	
	print "Formated adress: %s" % data['address']
	print "Latitude %f Longitude: %f" % (float(data['longitude']), float(data['latitude']))

# http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python

''' Returns -1 when the data is not valid.
	0 in other cases '''

def displayXML(data):

	tree  = readXML(data)
	valid = checkValidTree(tree)

	if (valid == -1): return -1

	root  = tree[1] # The 1 element in the array is the api result that we're going to parse

	parsedData = {}
	addresses = []
	parsedData = {
		"name": None, 
		"country": None,
		"address": None,
		"short_name": None, 
		"level_1_entity": None, 
		"latitude": None, 
		"longitude": None 
	}
	
	for elem in root:
		# print elem
		if (elem.tag == 'formatted_address'):
			
			parsedData['address'] = elem.text # save formated addres on the python dictionary
		
		elif(elem.tag == 'geometry'):
			
			location = elem.find('location') # Find the location element inside all the geometry tags
			parsedData['latitude'] = location.find('lat').text # Get latitud value of the object
			parsedData['longitude'] = location.find('lng').text

		elif(elem.tag == 'address_component'):
			
			childrenDict = {}
			
			for children in elem:
				childrenDict[children.tag] = children.text
				
			addresses.append(childrenDict)

	parsedData['name'] = addresses[0]['long_name']
	parsedData['country'] = addresses[-1]['long_name']
	parsedData['short_name'] = addresses[-1]['short_name']
	parsedData['level_1_entity'] = addresses[-2]['long_name']
	
	printInformation(parsedData)
		# print elem
	# print resultRoot[2].text


def callAPI(address):
	global googleXML_API

	# parameters = "address=" + address + "&sensor=" + sensor 
	parameters = urllib.urlencode({'address': address });
	url  = googleXML_API + parameters

	print "Calling " + url

	uh 	 = urllib.urlopen(url)
	data = uh.read();

	return data

	# print "Recuperados", len(data), 'characters'

	# e = xml.etree.ElementTree.parse(data).getroot()

''' Returns a string for the city inputted by the user '''
def introduceCity():
	valid = False

	while not valid:
		city = raw_input("Introduce your data: ")
		if city and city.isalpha():
			valid = True
		else:
			print '\t Come on! Numbers are not permited in this program :P'; 

	return city

def main():
	stop = False

	while not stop:

		city = introduceCity()

		if (city == 'stop'):
			stop = True # exit the program
		else:
			returnedData = callAPI(city);
			displayXML(returnedData)

	print "Exiting the program"

# data = '<GeocodeResponse><status>OK</status><result><type>locality</type><type>political</type><formatted_address>Madrid, Madrid, Spain</formatted_address><address_component><long_name>Madrid</long_name><short_name>Madrid</short_name><type>locality</type><type>political</type></address_component><address_component><long_name>Madrid</long_name><short_name>Madrid</short_name><type>administrative_area_level_4</type><type>political</type></address_component><address_component><long_name>Área Metropolitalitana y Corredor del Henares</long_name><short_name>Área Metropolitalitana y Corredor del Henares</short_name><type>administrative_area_level_3</type><type>political</type></address_component><address_component><long_name>Madrid</long_name><short_name>M</short_name><type>administrative_area_level_2</type><type>political</type></address_component><address_component><long_name>Community of Madrid</long_name><short_name>Community of Madrid</short_name><type>administrative_area_level_1</type><type>political</type></address_component><address_component><long_name>Spain</long_name><short_name>ES</short_name><type>country</type><type>political</type></address_component><geometry><location><lat>40.4167754</lat><lng>-3.7037902</lng></location><location_type>APPROXIMATE</location_type><viewport><southwest><lat>40.3120639</lat><lng>-3.8341618</lng></southwest><northeast><lat>40.5638447</lat><lng>-3.5249115</lng></northeast></viewport><bounds><southwest><lat>40.3120639</lat><lng>-3.8341618</lng></southwest><northeast><lat>40.5638447</lat><lng>-3.5249115</lng></northeast></bounds></geometry><place_id>ChIJgTwKgJcpQg0RaSKMYcHeNsQ</place_id></result></GeocodeResponse>'
# displayXML(data, outputFile)
main()	
