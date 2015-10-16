# -*- coding: utf-8 -*-
import csv

filename 			 = "PitchingPost.csv"
filenameAcummYears 	 = "AcumAnnos.cvs"
filenameAcummPlayers = "AcumJugadores.cvs"
filenameOrdered 	 = "Ordenado.cvs"

# Write the csv to a file.
def writeFile(data,filename, headerStr):
	valid = 0; # 0 means success | -1 = fails writing the file

	#TODO: Check if the file has .csv format. If not. Will return false
	try:
		outputFilename = filename; 
		outputFile = open(outputFilename, 'w')
		csvWriter = csv.writer(outputFile, delimiter=',', dialect='excel'); # http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file
	 	
	 	csvWriter.writerow(headerStr); # write the header to the csv file

	 	for key, value in data.iteritems():
			csvWriter.writerow([key, value]);

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
		# else
			# skip first elem

	headerStr = "year, frecuency"
	writtenFile = writeFile(frecuency, filenameAcummYears, headerStr); # export the list to 
	
	if (writtenFile == -1):
		print "Error writing a file"

def orderPlayers():
	global filename
	global filenameOrdered

	playerList = readCSV(filename); # loads player list from .csv file

	outputFile = open(filenameOrdered, "w");
	csvWriter = csv.writer(outputFile, delimiter=',', dialect='excel'); # http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file

	csvWriter.writerow(playerList[0]); # Write the header
	playerList  = sorted(playerList[1:]); # sorted player list (without header)

	for index, player in enumerate(playerList):
		csvWriter.writerow(player);


obtainYearFrecuency();
orderPlayers();
