# -*- coding: utf-8 -*-
import csv
import json

filename = "tweets.txt";
outputFile = "mostUsedHasgtags.csv";

# Returns a list of tweets
def loadTweets(filename):
	try:
		openedFile = open(filename, "r");
		tweetsList = []
		# i = -1;
		for line in openedFile:
			tweet = json.loads(line);
			if not tweet.has_key('delete'):
				tweetsList.append(tweet);
				# print str(i+1) + "It's added"
			# else:
				# skip deleted tweets
				# print str(i+1) + "It's deleeete"
			# i += 1
			# print str(i)
		openedFile.close();
		print "All twetts loading from file"
	except:
		print "Problems loading twetts from file"

	return tweetsList;

# Returns a dictionary for the hastagh frecuency
def createHashtagFrecuency(inputList):
	if (not isinstance(inputList, list)): 
		return None; #is not a Dictionary

	hashtagTable = {} # create empty dictionary

	for tweet in inputList:
		for hashtag in tweet['entities']['hashtags']:
			
			hashtagName = hashtag['text'];

			if (hashtagName in hashtagTable):
				hashtagTable[hashtagName] += 1;
			else:
				hashtagTable[hashtagName] = 1;

	return hashtagTable

def orderHashtagTable(dictionary):
	if (not isinstance(dictionary, dict)): 
		return None; #is not a Dictionary
	return sorted(dictionary.items(), key = lambda t:t[1], reverse=True);

# Write the csv to a file.
def writeFile(headerList, data, outputFile):
	valid = 0; # 0 means success | -1 = fails writing the file

	#TODO: Check if the file has .csv format. If not. Will return false
	try:
		outputFile = open(outputFile, 'w')
		csvWriter = csv.writer(outputFile, delimiter=',', dialect='excel'); # http://stackoverflow.com/questions/29335614/python-csv-writer-leave-a-empty-line-at-the-end-of-the-file	 	
	 	csvWriter.writerow(headerList); # write the header to the csv file

	 	for hashtag in data:
	 		csvWriter.writerow(hashtag);
	 	
		outputFile.close();

	except:
		valid = -1;

	return valid;

tweetsList = [] # list of tweetsList
tweetsList = loadTweets(filename);
hashtagTable = {}; # dictionary for the hashtag list
hashtagTable = createHashtagFrecuency(tweetsList);
orderedHashtagTable = orderHashtagTable(hashtagTable)

i = 0;
for hashtag in orderedHashtagTable[:10]:
	print str(hashtag[0]) + ", " + str(hashtag[1])


headerList = ["hashtag", "frecuency"]
writeFile(headerList, orderedHashtagTable[:10], outputFile);
