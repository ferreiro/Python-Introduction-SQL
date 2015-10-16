# -*- coding: utf-8 -*-
import csv

filename 			 = "PitchingPost.csv"
filenameAcummYears 	 = "AcumAnnos.cvs"
filenameAcummPlayers = "AcumJugadores.cvs"
filenameOrdered 	 = "Ordenado.cvs"

# Write the csv to a file.
def writeFile(data,filename):
	valid = 0; # 0 means success | -1 = fails writing the file
	i = 0;

	#TODO: Check if the file has .csv format. If not. Will return false
	try:
		outputFilename = filename; 
		outputFile = open(outputFilename, 'w')
		ofWriter = csv.writer(outputFile, delimiter=',', dialect='excel'); # http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file
	 
	 	for key, value in data.iteritems():
			ofWriter.writerow([key, value]) 
			i += 1 

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

def obtainYearFrecuency():
	global filename
	global filenameYearFrecuency

	frecuency = {} # dictionary to save the frecuncy for each year
	playerList = readCSV(filename); # loads player list from .csv file

	for index, player in enumerate(playerList):
		if(index >= 1):		
			year = str(player[1]) # index = 1, is the year field on csv
			if year in frecuency:
				frecuency[year] += 1;
			else:
				frecuency[year] = 1;
		# else
			# skip first elem

	writtenFile = writeFile(frecuency, filenameAcummYears); # export the list to 
	
	if (writtenFile == -1):
		print "Error writing a file"

obtainYearFrecuency();
