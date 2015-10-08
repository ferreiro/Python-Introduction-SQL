import json

filename = "test3.json"
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
		agenda = {"contacts" : []} # set empty dictionary

def saveUsers():
	global filename
	global agenda

	json_array = ''; # empty json object

	if (agenda == None):
		json_array = json.dumps({"contacts" : []}) # empty agenda object
		print "No object is created.\nWe're going to save and empty object\n"
	else:
		# format contacts dictionaty into json string
		json_array = json.dumps(agenda);
		print "Saving contacts in agenda"

	fileManager = open(filename, 'w');
	fileManager.write(str(json_array));


# loadUsers()

saveUsers()
print agenda
#print contacts[1]['name']
