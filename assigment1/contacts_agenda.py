import json

filename = "agenda.json"
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
		print "Problems... File not exist or BAD FORMAT!"
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

def createUser(user):
	global agenda

	name = str(user['name'])
	phone = int(user['phone'])
	surname1 = str(user['surname1'])
	surname2 = str(user['surname2'])

	if (agenda == None):
		# Agenda is empty, so create a new field
		agenda = {}
		contacts = []; # Array of "user" objects
		contacts.append(user);
		agenda['contacts'] = contacts;
		
	else:
		if(doesUserExists(user)):
			print "This user exits on Database"
		else:
			print "Your exist is not on the Data base. We're adding it ;-)"
			agenda['contacts'].append(user)

	print "\tUser added"

def doesUserExists(user):
	print "Sorry. But user exits"
	return True

#loadUsers()
#saveUsers()

newUser = {
	"name" : "Jorge",
	"surname1" : "Garcia",
	"surname2" : "Ferreiro",
	"phone" : "699600388"
}

createUser(newUser)
createUser(newUser)
print agenda
#print contacts[1]['name']
