import csv

filename = "PitchingPost.csv"

def writeFile(data,filename):
	# Write the csv to a file.
	outputFilename = filename + ".cvs"
	outputFile = open(outputFilename, 'w')
	ofWriter = csv.writer(outputFile, delimiter=',', dialect='excel')
 	
	i = 0

	# http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file
 
 	for key, value in data.iteritems():
		ofWriter.writerow([key, value]) 
		i += 1 

	outputFile.close()

# Read csv contacts

fs = open(filename)
reader = csv.reader(fs)
contacts = list(reader)

frecuency = {}

for index, player in enumerate(contacts):
	if(index >= 1):		
		year = str(player[1]) # index = 1, is the year field on csv
		if year in frecuency:
			frecuency[year] += 1;
		else:
			frecuency[year] = 1;
	# else
		# skip first elem



print len(contacts)




writeFile(frecuency,"AcumAnnos")