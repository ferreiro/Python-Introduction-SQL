import json

filename = "test1.json"
agenda = None #dictionary for saving all agenda (contacts, whatever)

# Load users from JSON into a dictionary
def loadUsers():
	global filename
	global agenda

	try:
		data = open(filename, 'r'); # try to open JSON file
		jsonData = json.load(data) # parse json object
		agenda = jsonData # save agenda object into global variable "agenda"
	except:
		print "File not found! No problem dude. We're creating and empty list"
		agenda = '{"contancts" : []}' # set empty dictionary

def saveUsers():
	global contacts

	json_array = ''; # empty json object

	if (contacts == None):
		json_array = '{"agenda" : []}' # empty agenda object
	else:
		# format contacts dictionaty into json string
		json_array += json.dumps(contacts);
		print json_array

	fileManager = open('test2.json', 'a');
	fileManager.write(json_array);


loadUsers()
# saveUsers()
#print contacts[1]['name']
