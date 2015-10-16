# -*- coding: utf-8 -*-
import csv

filename 			 = "PitchingPost.csv"
filenameAcummYears 	 = "AcumAnnos.cvs"
filenameAcummPlayers = "AcumJugadores.cvs"
filenameOrdered 	 = "Ordenado.cvs"

# Write the csv to a file.
def writeFile(headerList, data, filename):
	valid = 0; # 0 means success | -1 = fails writing the file

	#TODO: Check if the file has .csv format. If not. Will return false
	try:
		outputFile = open(filename, 'w')
		csvWriter = csv.writer(outputFile, delimiter=',', dialect='excel'); # http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file	 	
	 	csvWriter.writerow(headerList); # write the header to the csv file

	 	for index, player in enumerate(data):
			csvWriter.writerow(player);

		outputFile.close();

	except:
		valid = -1;

	return valid;

def readCSV(filename):

	#TODO: Check if the file has .csv format. If not. Will return false
	# Read csv contacts
	fs = open(filename)
	reader = csv.reader(fs)
	contacts = list(reader)

	return contacts;

def convertDictToList(inputDictionary):
	if (not isinstance(inputDictionary, dict)): 
		return None; #is not a Dictionary

	# it's a Dictionary
	newList = []

	for key, value in inputDictionary.iteritems():
		aux = [key, value]
		newList.append(aux);

	return newList; # correct conversion

# TODO: return -1 or 0 if the function fails
def obtainYearFrecuency():
	global filename
	global filenameAcummYears

	frecuency = {} # dictionary to save the frecuncy for each year
	playerList = readCSV(filename); # loads player list from .csv file

	for index, player in enumerate(playerList):
		if(index >= 1):		
			year = str(player[1]) # index = 1, is the year field on csv
			if year in frecuency:
				frecuency[year] += 1;
			else:
				frecuency[year] = 1;
		#else:
			# skip the header

	headerList = ["year", "frecuency"]
	yearFrecuncyList = convertDictToList(frecuency);

	writtenFile = writeFile(headerList, yearFrecuncyList, filenameAcummYears); # export the list to 
	
	if (writtenFile == -1): print "Error writing a file"


def obtainPlayerFrecuency():
	global filename
	global filenameAcummPlayers

	playerFrecuency = {} # dictionary to save the frecuency for each Player
	playerList = readCSV(filename); # loads player list from .csv file

	for index, player in enumerate(playerList):
		if(index >= 1):		
			Player = str(player[0]) # index = 0, is the PlayerId field on csv
			if Player in playerFrecuency:
				playerFrecuency[Player] += 1;
			else:
				playerFrecuency[Player] = 1;
		# else
			# skip first elem

	headerList = ["player", "frecuency"]
	playerFrecuencyList = convertDictToList(playerFrecuency);

	writtenFile = writeFile(headerList, playerFrecuencyList, filenameAcummPlayers); # export the list to 
	
	if (writtenFile == -1):
		print "Error writing a file"

def orderPlayers():
	global filename
	global filenameOrdered

	csvFile = readCSV(filename); # loads player list from .csv file
	headerList = csvFile[0]; # loading header from the list
	playerList  = sorted(csvFile[1:]); # sorted player list (without header)

	writeFile(headerList, playerList, filenameOrdered);

orderPlayers();
obtainYearFrecuency();
obtainPlayerFrecuency();
