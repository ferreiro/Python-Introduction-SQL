
# Basic data type.
agenda = {}
contacts = []

def loadContacts():
	print "TODO"

def createEntry(entry):
	print "TODO"

def deleteEntry(entry):
	print "TODO"

def updateEntry(entry):
	print "TODO"

def findEntry(entry):
	print "TODO"
	return -1; # returns index of the elements

def menu():
	option = -1;
	print "Select an option"
	option = raw_input("...");

	if option == "option":
		option = -1
	else:
		option = 1

	return option; # exit the menu

def main():
	global agenda
	global contacts

	loadContacts()

	while (option = menu()) not -1:
		option = menu();

	saveContacts() # save when exist the program

main()