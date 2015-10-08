import json

filename = "agenda.json";
contacts = []; #dictionary for saving all contacts

# Load users from JSON into a dictionary
def loadUsers():
	global contacts

	try:
		fileData = open(filename, 'r')
		tmpContacts = json.load(fileData)
		contacts = tmpContacts['contacts'] # Save contacts in global variable
	except:
		print "File not found"
		contacts = [{}] # set empty dictionary

loadUsers();
print contacts[1]
