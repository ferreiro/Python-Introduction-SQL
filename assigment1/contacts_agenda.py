import os
import json

# Global variables

filename = "agenda.json"
agenda   = {} #dictionary for saving all agenda (contacts, whatever)
messages = {
	"system" : "[ System ]",
	"warning" : "[ Warning ]",
	"problem" : "[ Problem ]",
	"success" : "[ OK ]"
}

# Load users from JSON into a dictionary
def loadUsers(filename):
	global agenda
	global messages

	try:
		data = open(filename, 'r'); # try to open JSON file
		jsonData = json.load(data) # parse json object into python dictionary
		agenda = jsonData # save agenda object into global variable "agenda"
		print messages['system'] + " Contacts loaded"
	except:
		agenda['contacts'] = [] # set empty dictionary
		print messages['warning'] + " Problems... File not exist or BAD FORMAT!"
		print messages['system'] + " We're creating an empty list\n"

def saveUsers(filename):
	global messages
	global agenda

	if agenda == None or agenda == {}:
		agenda['contacts'] = [] # empty array for contacts
		print messages['warning'] + " No object is created.\nWe're going to save and empty object\n"
	else:
		# format contacts dictionaty into json string
		print messages['system'] + " Saving contacts in agenda..."

	json_array = json.dumps(agenda) # empty agenda object
	fileManager = open(filename, 'w');
	fileManager.write(json_array);

""" Create user: add an user to the databse only if the user is not already created in our system. In other case, will return false """
def createUser(user):
	global messages
	global agenda

	created = True

	if agenda == None or agenda == {}:
		# Creating a new contacts field on dictionary agenda and add the user
		agenda = {} # Agenda is empty, so create a new contacts field
		tmpContacts = []
		tmpContacts.append(user);
		agenda['contacts'] = tmpContacts # saving on dictionary
		print messages['success'] + " User added to the agenda \n"

	else:
		contacts = agenda['contacts']

		if not existContact(user):
			contacts.append(user)
			print messages['success'] + " This user is not on our database. We're adding it ;-)"
		else:
			created = False
			print messages['warning'] + " Not added! This user is already on the Database"

def userIndex(user, contacts):
	index = -1 # Not found

	found = False
	i = 0

	while not found and i < len(contacts):
		# phone is going to be my primary key (Two users can't have the same phone)
		if(contacts[i]['name'] == user['name'] and contacts[i]['surname1'] == user['surname1'] and contacts[i]['surname2'] == user['surname2'] and contacts[i]['phone'] == user['phone']):
			found = True
			index = i
		i += 1;

	return index

def existContact(user):
	global agenda

	contacts = agenda['contacts']
	index = userIndex(user, contacts);
	
	if (index == -1):
		return False
	else:
		return True

def updateUser(user):
	global agenda

	updated = True
	contacts = agenda['contacts']

	index = userIndex(user, contacts)

	if (index != -1): 
		contacts[index]['name'] = user['name']
		contacts[index]['phone'] = user['phone']
		contacts[index]['surname1'] = user['surname1']
		contacts[index]['surname2'] = user['surname2']
	else:
		updated = False # user doesn't exist

	return updated

def deleteUser(user):
	global agenda

	deleted = False
	contacts = agenda['contacts']
	index = userIndex(user, contacts);

	if index >= 0:
		contacts.pop(index)
		deleted = True

	return deleted

def deleteLastUser():
	global agenda

	contacts = agenda['contacts']
	deleted = False

	if len(agenda['contacts']) >= 1:
		deleted = True
		contacts.pop();

	return deleted;

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def introduceUser():
	name = raw_input("name: ");
	surname1 = raw_input("surname1: ");
	surname2 = raw_input("surname2: ");
	phone = raw_input("phone: ");

	newUser = {
		"name" : name,
		"surname1" : surname1,
		"surname2" : surname2,
		"phone": phone
	}

	return newUser

def printUser(user):
	for data in user:
		print data

def search():
	global agenda

	contacts = agenda['contacts']

	print "What do you want to Search?"
	print "Valid answers: all, name, phone, surname1, surname2"

	valid = False
	toSearch = ""
	user = {
		"name" : "",
		"surname1" : "",
		"surname2" : "",
		"phone" : ""
	}

	while not valid:
		toSearch = str(raw_input()).lower
		valid = True

		if (toSearch == "all"):
			user = introduceUser()
		
		elif (toSearch == "name"):
			user['name'] = str(raw_input("What is the name? "));
		
		elif (toSearch == "phone"):
			user['phone'] = str(raw_input("What is the phone? "));
			
		elif (toSearch == "surname1"):
			user['surname1'] = str(raw_input("What is the surname1? "));

		elif (toSearch == "surname2"):
			user['surname2'] = str(raw_input("What is the surname2? "));
		
		else:
			valid = False

	index = userIndex(user, contacts)
	
	if (index != -1):
		print "User found!"
		printUser(user)
	else:
		print "User is not found"




""" Returns a user created by the user """
def introduceSearch():
	user = {}
	name = "";
	surname1 = "";
	surname2 = "";
	phone = "";

	the_name = raw_input("Search by name?: [yes/no]")
	if (the_name == "yes"): name = raw_input("Name: ");
	
	the_phone = raw_input("Search also by phone?: [yes/no]")
	if (the_phone == "yes"): phone = raw_input("phone: ");

	surname = raw_input("Search also by surname 1?: [yes/no]")
	if (surname == "yes"): surname1 = raw_input("surname 1: ");

	surname = raw_input("Search also by surname 2?: [yes/no]")
	if (surname == "yes"): surname2 = raw_input("surname 2: ");

	user = {
		"name" : name,
		"surname1" : surname1,
		"surname2" : surname2,
		"phone": phone
	}

	return user

def menu():
	option = ""

	print "----------- MENU -----------" 
	print "create (create entry)"
	print "delete (delete the last one entry)"
	print "deleteUser (delete one user)"
	print "search (search entry)"
	print "exit (close program)"
	print "----------------------------" 

	return str(raw_input("Your option? ")).lower()


def menu2():
	global agenda

	contacts = agenda['contacts']
	exit = False;


	input = str(raw_input("Your option? "));
	input.lower()

	# to lower
	cls()

	if(input == "create"):
		newUser = introduceUser();
		createUser(newUser);
	elif(input == "delete"):
		deleted = deleteLastUser();
		if(deleted):
			print "deleted"
		else:
			print "[0] contacts you can't delete"
	elif(input == "deleteuser"):
		user = introduceUser()
		deleted = deleteUser(user)
		if (deleted):
			print "User deleted"
		else:
			print "User not deleted"

	elif(input == "search"):

		user = introduceSearch()
		index = userIndex(user, contacts)

		if (index == -1):
			print "This user doesn't exist on our database"
		else:
			print "Info for your user"
			for line in user:
				print line

	elif input=="exit":
		exit = True;

	return exit;


def main():
	global agenda
	global filename

	cls() # clear the screen
	exit = False
	loadUsers(filename) # load users

	while not exit:

		print agenda['contacts']
		option = menu()
		cls() # clear the screen 

		if (option == "exit"):
			exit = True

		elif (option == "create"):
			newUser = introduceUser()
			createUser(newUser)

		elif (option == "delete"):
			if (deleteLastUser()):
				print messages['success'] + " user deleted!"
			else:
				print messages['warning'] + " user not deleted because there are not any user on the DB!"

		elif (option == "deleteuser"):
			print "delete an user"
		elif (option == "search"):
			search()
		elif (option == "deleteuser"):
			print "update"
		elif (option == "deleteuser"):
			print "delete User"
		else:
			print "Error. Command not found"

	saveUsers(filename) # load users



main()