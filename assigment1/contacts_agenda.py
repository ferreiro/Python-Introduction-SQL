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

def validUser(user):
	return False;

def createUser(user):
	global agenda

	if (agenda == None):
		# Agenda is empty, so create a new field
		agenda = {}
		contacts = []; # Array of "user" objects
		contacts.append(user);
		agenda['contacts'] = contacts;
		print "User created on the agenda \n"
		
	else:
		contacts = agenda['contacts']
		if(doesContactExists(user)):
			print ">This user exits on Database"
			print ">>We're updating this user data... :-)"
			index = userIndexInArray(user, contacts)
			updateUser(user, index, contacts);
		else:
			print ">Your exist is not on the Data base. We're adding it ;-)"
			agenda['contacts'].append(user)
			print "\tUser added"

def deleteUser(user):
	print "Coming soon"

def deleteLastUser():
	global agenda
	agenda['contacts'].pop();

def userIndexInArray(user, contacts):
	index = -1 # Not found
	i = 0
	found = False

	while not found and i < len(contacts):
		# phone is going to be my primary key (Two users can't have the same phone)
		
		if(contacts[i]['phone'] == user['phone'] and contacts[i]['name'] == user['name']):
			found = True
			index = i
		i += 1;

	return index

def doesContactExists(user):
	global agenda
	contacts = agenda['contacts']

	index = userIndexInArray(user, contacts);
	
	if (index == -1):
		return False
	else:
		return True

def updateUser(user, index, contacts):
	if (index == -1):
		return

	contacts[index]['name'] = user['name']
	contacts[index]['phone'] = user['phone']
	contacts[index]['surname1'] = user['surname1']
	contacts[index]['surname2'] = user['surname2']

def menu():
	exit = False;

	print "create (create entry)"
	print "delete (delete the last one entry)"
	print "search (search entry)"
	print "load entry (load entry)"
	print "exit (close program)"

	input = str(raw_input());
	# to lower

	if(input == "create"):
		name = raw_input("name: ");
		phone = raw_input("phone: ");
		surname1 = raw_input("surname1: ");
		surname2 = raw_input("surname2: ");

		newUser = {
			"name" : name,
			"surname1" : surname1,
			"surname2" : surname2,
			"phone": phone
		}
		createUser(newUser);
	elif(input == "delete"):
		deleteLastUser();
		print "deleted"
	elif(input == "search"):
		name = '';
		surname1 = '';
		surname2 = '';
		phone = '';

		the_name = raw_input("Search by name?: [yes/no]")
		if (the_name == "yes"): name = raw_input("Name: ");
		
		the_phone = raw_input("Search also by phone?: [yes/no]")
		if (the_phone == "yes"): phone = raw_input("phone: ");

		surname = raw_input("Search also by surname 1?: [yes/no]")
		if (surname == "yes"): surname1 = raw_input("surname 1: ");

		surname = raw_input("Search also by surname 2?: [yes/no]")
		if (surname == "yes"): surname2 = raw_input("surname 2: ");

		newUser = {
			"name" : name,
			"surname1" : surname1,
			"surname2" : surname2,
			"phone": phone
		}
		i = 0;
		while i < len(agenda['contacts']):
			index = userIndexInArray(newUser, agenda['contacts'])
			if (index != -1): print agenda['contacts'][index]
			i += 1;

	elif input=="exit":
		exit = True;

	return exit;



loadUsers();
exit = False

while not exit:
	exit = menu();

saveUsers();