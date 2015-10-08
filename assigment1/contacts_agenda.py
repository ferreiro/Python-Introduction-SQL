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
		print "User created on the agenda \n"
		
	else:
		if(doesContactExists(user)):
			print ">This user exits on Database"
			print ">>We're updating this user data... :-)"
			updateUser(user);
		else:
			print ">Your exist is not on the Data base. We're adding it ;-)"
			agenda['contacts'].append(user)
			print "\tUser added"

def doesContactExists(user):
	global agenda
	contacts = agenda['contacts']
	found = False;
	i = 0

	while not found and i < len(contacts):
		# phone is going to be my primary key (Two users can't have the same phone)
		
		if(contacts[i]['phone'] == user['phone'] and contacts[i]['name'] == user['name']):
			found = True
		# else: "phone not matching"

		i += 1;
	return found

def updateUser(user):
	print "Updating user"

loadUsers()
#saveUsers()

newUser = {
	"name" : "Jorge",
	"surname1" : "Garcia",
	"surname2" : "Ferreiro",
	"phone" : "699600388"
}
newUser2 = {
	"name" : "Paco",
	"surname1" : "Gracia",
	"surname2" : "Jimenez",
	"phone" : "20202"
}
newUser3 = {
	"name" : "Alvaro",
	"surname1" : "Gonzale",
	"surname2" : "Jimenez",
	"phone" : "30303030"
}

createUser(newUser)
createUser(newUser2)
createUser(newUser3)


saveUsers()
#print contacts[1]['name']
