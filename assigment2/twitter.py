# -*- coding: utf-8 -*-
import csv
import json

outdirectory 	= "outputCSV/"
tweetsFile 		= "tweets.txt";
outputFile 		= "mostUsedHasgtags.csv";

tweetsList = [] # List that contains all the tweets readed from a file
hashtagTable = {}; # Dictionary with key= hashtags and value= frecuency for this hashtag 

# Returns a list of tweets
def loadTweets(inputFilename):

	tweetsList = [] # returns a list of tweets
	successMsg = "Loading twetts from file...";

	try:
		openedFile = open(inputFilename, "r");
		
		for line in openedFile:
			tweet = json.loads(line);
			if not tweet.has_key('delete'):
				tweetsList.append(tweet);
			# else: skip objects with "delete" key

		print successMsg + "[OK]"
		openedFile.close(); # Close the file

	except:
		print successMsg + "[ERROR]"

	return tweetsList;

# Returns a dictionary for the hastagh frecuency
def createHashtagFrecuencyTable(inputList):

	if (not isinstance(inputList, list)): 
		return None; # exit function if the input object is not a list

	hashtagTable = {} # create empty dictionary

	for tweet in inputList: # iterate all the tweets loaded in the list
		for hashtag in tweet['entities']['hashtags']: # iterate all the hastags for each tweet
			
			hashtagName = hashtag['text']; # Get a hashtag from the weet

			if (hashtagName in hashtagTable): 
				hashtagTable[hashtagName] += 1; # Hashtag was previously added to the dictionary. Increase value by one
			else:
				hashtagTable[hashtagName] = 1; # Hashtag wasn't in the directionary. Add it with 1 value

	return hashtagTable

def orderHashtagTable(dictionary):
	if (not isinstance(dictionary, dict)): 
		return None; # exit function if the input object is not a dictionay
	return sorted(dictionary.items(), key = lambda t:t[1], reverse=True);

# Write the csv to a file.
def writeFile(headerList, data, outputFile):
	
	valid = 0; # 0 means success | -1 = fails writing the file
	successMsg = "Writing to file...";

	if not outputFile.endswith(".csv"): # Check if the file has .csv format. If not. Will return false
		
		print "Outpufile extension %s not valid" % (outputFile[-4:]) # Notify file output extension doesn't exist
		print successMsg + "[ERROR]"
		return -1; # output file format not valid
	
	try:

		outputFile 	= open(outputFile, 'w')
		csvWriter 	= csv.writer(outputFile, delimiter=',', skipinitialspace=True, dialect='excel'); # http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file	 	
	 	csvWriter.writerow(headerList); # write the header to the csv file

	 	for hashtag in data:
	 		csvWriter.writerow(hashtag);
	 	
		outputFile.close();

		print successMsg + "[OK]"

	except: 

		print successMsg + "[ERROR]"
		valid = -1; # Problems writting the file

	return valid;

tweetsList = loadTweets(tweetsFile);
hashtagTable = createHashtagFrecuencyTable(tweetsList);
orderedHashtagTable = orderHashtagTable(hashtagTable)

headerList = ["hashtag", "frecuency"] # .csv header to write on the file
writeFile(headerList, orderedHashtagTable[:10], outputFile);
