
# Chechinput: returns false is the inputed text 
# has any numeric character

def checkInput(userInput):
	return userInput.isalpha()
 
# CheckNumber: returns false is the inputed text 
# has any numeric character

def checkNumber(userInput):
	return userInput.isdigit()

def readMessage():
	valid = False; 
	message = '';
	while(not valid):
		# Iterate until input message has not have any numeric element (number)
		message = raw_input('Introduce your message: ');
		valid = checkInput(message);

	return message;

# Now, let the user inputs the desired shift number
# iterates until inputed number is correct.

def readNumber():
	valid = False;
	number = -1;
	while(not valid):
		number = raw_input('Introduce your shift Number: ');
		valid = checkNumber(number);
		if (not valid):
			print 'Come on! this is not a number :P'; 

	return number;

# Returns and object with a message and a number.

def userInput(): 
	message = readMessage();
	number = readNumber(); 

	# Compose and object and returns to the user
	userInput = {'message': message, 'number': number};
	return userInput;

def simpleEncription(message, shiftNumber):
	
	if (type(shiftNumber) is not int):
		shiftNumber = int(shiftNumber); # Int casting of shiftNumber when typed is not expressed as integer. Sometimes may ocurr the program interprets a string...
	
	auxChar = '';
	encriptedMsg = list();
	shiftNumber = shiftNumber % 26; # English alfhabet has 26 elements. when user shifs more than 26, then make the modulus! if not, an error will crash lines below.

	# Convert each character of the array into a
	# number, then sum the shif and finally convert this
	# number into the alfabhet letter corresponding.
	 
	for char in message:
		
		if (char == 'z'):
			auxChar = ord('a') - 1;
		elif (char == 'Z'):
			auxChar = ord('A') - 1;
		else:
			auxChar = ord(char);

		auxChar += shiftNumber;
		encriptedChar = chr(auxChar);
		encriptedMsg.append(encriptedChar);

	return encriptedMsg;


userInput = userInput(); # Returns a valid message and shif number from user in a list.
message = userInput['message']; # Local variable for the message inputed by the user
number = userInput['number']; # Local variable for the number inputed by the user

encriptedMsgList = simpleEncription(message, number);

print encriptedMsgList

outputMsg = '';
for index, char in enumerate(encriptedMsgList):
	outputMsg += char;

print outputMsg
