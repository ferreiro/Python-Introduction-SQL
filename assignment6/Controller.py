import sqlite3
import re
import json
import random
from bottle import request, route, run, template, response, static_file;
from datetime import datetime
from passlib.hash import sha256_crypt

dbfile = "notes.sqlite3";
conn   = sqlite3.connect(dbfile);

def openCursor():
	global conn
	cursor = conn.cursor();
	return cursor;

def closeCursor(cursor):
	cursor.close();

# Change for cookies
sessionUser = None; # Empty Dictionary. Updated when login and erased when logout. 


# Static Routes
@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/')


#################################
############AUXILIAR FUNCTIONS #############
#################################

def encriptpassword(Password):
	hash = sha256_crypt.encrypt(Password)
	return hash

def verifyPassword(Password, hash):
	return sha256_crypt.verify(Password,hash);


def makeEmptySessionUser():
	emptyUser = {
		"UserID" : '',
		"Email" : '',
		"Username" : '',
		"Name" : '',
		"Surname" : '',
		"Birthday" : '',
		"City" : '',
		"Premium" : ''
	}
	return emptyUser;
def setSessionUser(user):
	global sessionUser

	try:
		if (user != None):
			#print user
			sessionUser = {
				"UserID" : user['UserID'],
				"Email" : user['Email'],
				"Username" : user['Username'],
				"Name" : user['Name'],
				"Surname" : user['Surname'],
				"Birthday" : user['Birthday'],
				"City" : user['City'],
				"Premium" : user['Premium']
			}
			#print user;
			#print sessionUser;
	except:
		#print sessionUser
		print "Can't set the user session"
		return False; # Coudln't set a session user

	return True; # set!

def validUser(user):
	return (user != None);


#####
####GETTING USER OBJECTS
#####

def getUserbyEmailPassword(email, password):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.Email='"+str(email)+"' And User.Password='"+str(password) + "'";
		cursor.execute(query); # Check if the email and password exists on our database
		user = cursor.fetchone(); # Get the returned object for the database
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;

def getUserbyUsername(username):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.Username='"+str(username)+"'";
		cursor.execute(query); # Check if the email and password exists on our database
		user_tuple = cursor.fetchone(); # Get the returned object for the database
		user = usertupleToDictionary(user_tuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;


def getUserbyEmail(Email):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.Email='"+str(Email)+"'";
		cursor.execute(query); # Check if the email and password exists on our database
		user_tuple = cursor.fetchone(); # Get the returned object for the database
		user = usertupleToDictionary(user_tuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;


def getUserbyID(id):
	user   = None;
	cursor = openCursor();
	try:
		query = "Select * from User where User.UserID='"+str(id)+"'";
		cursor.execute(query); # Check if the email and password exists on our database
		user_tuple = cursor.fetchone(); # Get the returned object for the database
		user = usertupleToDictionary(user_tuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return user;


#####
####GETTING NOTES OBJECTS
#####

def getNotebyNoteID(NoteID):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.NoteID="+str(NoteID);
		cursor.execute(query); # Check if the email and password exists on our database
		noteTuple = cursor.fetchone(); # Get the returned object for the database
		note = notetupleToDictionary(noteTuple);
		#print note;
		closeCursor(cursor);
	except:
		print "Can't get notes given a userID and NoteID"

	return note;

def getNotebyPermalink(Permalink):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.Permalink='"+str(Permalink)+"'";
		#print query
		cursor.execute(query); # Check if the email and password exists on our database
		noteTuple = cursor.fetchone(); # Get the returned object for the database
		note = notetupleToDictionary(noteTuple);
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return note;

def getNoteby_Username_Permalink(Username, Permalink):
	note   = None;
	cursor = openCursor();
#try:
	query = "Select * from Notes join User where User.Username='"+str(Username)+"' And Notes.Permalink='"+str(Permalink)+"'";
	print query
	cursor.execute(query); # Check if the email and password exists on our database
	noteTuple = cursor.fetchone(); # Get the returned object for the database
	note = notetupleToDictionary(noteTuple);
	closeCursor(cursor);
#except:
	print "Can't get notes by this UserID and Permalink"

	return note;

#####
####GETTING COLORS OBJECTS
#####
""" Get all the avaliable colors for our database """
def getColorsAvailable():
	availableColors = []; # array of dictionaries
	cursor = openCursor();
	try:
		query = "Select * from Colors";
		cursor.execute(query); # Check if the email and password exists on our database
		colors = cursor.fetchall(); # Get the returned object for the database
		
		for color in colors:
			colorDict = {
				'Name' : color[0],
				'Color': color[1]
			}
			availableColors.append(colorDict);

		closeCursor(cursor);
	except:
		availableColors = None
		print "Can't retrieve all the colors"

	return availableColors;


""" Get all the avaliable colors for our database """
def getColorFromNote(NoteID):
	color = "";
	cursor = openCursor();
	try:
		query = "Select Name from Colors join Notes where NoteID=" + str(NoteID);
		cursor.execute(query); # Check if the email and password exists on our database
		color = cursor.fetchone()[0]; # Get the returned object for the database
		
		closeCursor(cursor);
	except:
		print "Can't retrieve color for noteID"

	return color;


# FetchAll notes for a given user id
# Add all the notes returned by the query into a list

def validNotes(notes):
	return (notes != None);

# Convert a note as a tuple into a Dictionary and return it

def usertupleToDictionary(_tuple):
	if (type(_tuple) != tuple):
		return None;

	user = {} # Return a Dictionary with a NOTE

	try:
		user['UserID'] = _tuple[0]
		user['Email'] = _tuple[1]
		user['Password'] = _tuple[2]
		user['Username'] = _tuple[3]
		user['Name'] = _tuple[4]
		user['Surname'] = _tuple[5]
		user['Birthday'] = _tuple[6]
		user['City'] = _tuple[7]
		user['Premium'] = _tuple[8]
	except:
		user = None; # invalid. Return empty

	return user;

def notetupleToDictionary(_tuple):
	if (type(_tuple) != tuple):
		return None;
	
	note = {} # Return a Dictionary with a NOTE

	try:
		note['NoteID'] 		= _tuple[0]
		note['UserID'] 		= _tuple[1]
		note['Title'] 		= _tuple[2]
		note['Permalink'] 	= _tuple[3]
		note['Content'] 	= _tuple[4]
		note['CreatedAt'] 	= _tuple[5]
		note['EditedAt'] 	= _tuple[6]
		note['Published']	= _tuple[7]
		note['Private'] 	= _tuple[8]
		note['Color'] 		= _tuple[9]
	except:
		note = None;

	return note;

def getNotesByUserID(UserID):
	notes_arr = []; # Array of dictionary (with notes)
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.UserID=" + str(UserID) + " ORDER BY CreatedAt DESC";
		#print query
		cursor.execute(query); # Check if the email and password exists on our database
		notes_tuples = cursor.fetchall(); # Get tuples returned by database
		
		# notes are tuples. So convert to dict and add to Notes array
		for n in notes_tuples:
			convertedNote = notetupleToDictionary(n); # tuple to dictionary
			query = "Select * from Colors where Colors.Name='"+convertedNote['Color']+"'";
			#print query
			cursor.execute(query);
			convertedNote['Color'] = cursor.fetchone()[1]
			notes_arr.append(convertedNote); # Append dictionary

		closeCursor(cursor);

	except:
		print "Can't retrieve a notes"

	return notes_arr;

""" Create a user in the database if the user doesn't exist """

def createUserDB(newUser):
	cursor = openCursor();

	encriptedPassword = encriptpassword(newUser['password']);
	print encriptpassword
	try:
		userString  = ("NULL,");
		userString += ("'" + str(newUser['email']) + "',");
		userString += ("'" + str(encriptedPassword) + "',");
		userString += ("'" + str(newUser['username']) + "',");
		userString += ("'" + str(newUser['name']) + "',");
		userString += ("'" + str(newUser['surname']) + "',");
		userString += ("'" + str(newUser['birthday']) + "',");
		userString += ("'" + str(newUser['city'])     + "',");
		userString += str(newUser['premium']);

		#print userString

		query = "Insert into User values(" + userString + ')';
		cursor.execute(query);
		conn.commit();
		closeCursor(cursor);

		return True;

	except:
		return False;


""" Create a user in the database if the user doesn't exist """

def createNoteDB(newNote):
	cursor = openCursor();
	#print "Oh tes"
	try:
		userString  = ("NULL,");
		userString += str(newNote['UserID']) + ",";
		userString += ("'" + str(newNote['Title']) + "',");
		userString += ("'" + str(newNote['Permalink']) + "',");
		userString += ("'" + str(newNote['Content']) + "',");
		userString += ("'" + str(newNote['CreatedAt']) + "',");
		userString += ("'" + str(newNote['EditedAt']) + "',");
		userString += (str(newNote['Published']) + ",");
		userString += (str(newNote['Private']) + ",");
		userString += ("'" + str(newNote['Color']) + "'");

		query = "Insert into Notes values(" + userString + ')';
		#print query
		cursor.execute(query);
		conn.commit();
		closeCursor(cursor);

		return True;

	except:
		return False;

def updatedBD(updatedNote):
	cursor = openCursor();

	query  = "Update Notes SET "
	query += "Title ='" + str(updatedNote['Title']) + "',  ";
	query += "Color ='" + str(updatedNote['Color']) + "', ";
	query += "Content ='" + str(updatedNote['Content']) + "', ";
	query += "Private =" + str(updatedNote['Private']) + ", ";
	query += "EditedAt ='" + str(updatedNote['EditedAt']) + "'";
	query += " where Notes.NoteID=" + str(updatedNote['NoteID']);
	query += " and Notes.UserID=" + str(updatedNote['UserID']);

	#print query

	cursor.execute(query);
	conn.commit();
	closeCursor(cursor);

	return True; # Updated.

def deleteNote(NoteID):
	try:
		cursor = openCursor();
		query  = "delete from Notes where notes.NoteID=" + str(NoteID) + ""
		cursor.execute(query);
		conn.commit();
		closeCursor(cursor);
	except:
		return False; #print "somethings go wrong"

	return True; # We delete a note succesfully

def updateUser(user):
#try:
	cursor = openCursor();

	query  = "Update User SET "
	query += "Name ='" + str(user['Name']) + "',  ";
	query += "Surname ='" + str(user['Surname']) + "', ";
	query += "Birthday ='" + str(user['Birthday']) + "', ";
	query += "City ='" + str(user['City']) + "'";
	query += " where User.UserID=" + str(user['UserID']);
	print query

	cursor.execute(query);
	conn.commit();
	closeCursor(cursor);
#except:
#	return False;

	return True;

def searchNotesFromUser(Keyword,UserID):
	if (Keyword == None or UserID == None):
		return [];

	MatchedNotes = []
	
	cursor = openCursor();
	query  = "select * from Notes where "
	query += "Notes.Title like '%"+ str(Keyword) +"%' ";
	query += "or Notes.Content like '%"+ str(Keyword) +"%' ";
	

	cursor.execute(query);
	#print query

	for _tuple in cursor.fetchall():
		convertedNote = notetupleToDictionary(_tuple); # tuple to dictionary
		MatchedNotes.append(convertedNote)
		#print convertedNote

	closeCursor(cursor);
	return MatchedNotes

#################################
############ROUTES #############
#################################

def redirectHome():
	global sessionUser
	response.status = 303
	response.set_header('Location', '/');
	return template('login', user=sessionUser); #Show login screen

def redirect(url):
	response.status = 303
	response.set_header('Location', '/'+ url);

def redirectLogin():
	response.status = 303
	response.set_header('Location', '/login');
	return template('login'); #Show login screen

def loginSuccessRedirect():
	global sessionUser
	response.status = 303
	response.set_header('Location', '/'+str(sessionUser['Username']));
	return profile(sessionUser['Username']);

@route('/logout')
def logout():
	global sessionUser
	sessionUser = sessionUser or None;

	if (sessionUser != None):
		copySession = sessionUser;
		sessionUser = None; # delete cookies or session information (in this case sessionUser object)
		del copySession # delete the other variable for security reassongs
	return redirectHome();

@route('/')
@route('/login')
def loginWindow():
	global sessionUser
	if (sessionUser == None):
		return template('login', user=sessionUser); #Show login screen
	else:
		return loginSuccessRedirect();

@route('/login', method='POST')
def login():
	global sessionUser

#try:
	email    = request.forms.get('email');
	password = request.forms.get('password');

	user = getUserbyEmail(email);
	
	if (user == None):
		print "user is None"
		return template('login-fail', user=None);

	if verifyPassword(password, user['Password']):
		setSessionUser(user); # set User session object
	else:
		return "The user is NOT valid!";
#except:
	#print "Problems with your query. Sorry..."

	return loginSuccessRedirect();

######### Register 
@route('/register')
def register():
	global sessionUser
	if (sessionUser == None):
		return template('signup', editUser=False, user=sessionUser); #Show login screen
	else:
		return loginSuccessRedirect();

@route('/register', method='POST')
def registerUserDatabase():
	#Dictionary with information for new user (following database model)
	newUser = {
		"UserID": None,
		"email" : request.forms.get('emailsignup'),
		"password" : request.forms.get('passwordsignup'),
		"name": request.forms.get('namesignup'),
		"surname": request.forms.get('surnamesignup'),
		"username": request.forms.get('usernamesignup'),
		"birthday": request.forms.get('birthdaysignup'),
		"city": request.forms.get('citysignup'),
		"premium": 0
	}

	if createUserDB(newUser): # user created successfully
		global sessionUser
		return template('signup-success', user=sessionUser);
	else:
		return "Problems creating user"
		print "Problems inserting a user on the database. Sorry..."
		return "Problems on the database"

#####SEARCH

@route('/search', method='POST')
@route('/search?q=<Keyword>', method="POST")
#@route('/search/<name>', method='GET')
def searchOnNotes():
	global sessionUser
	if (sessionUser == None):
		return template('login', user=None)

	user = getUserbyID(sessionUser['UserID'])

	if (user != None):
		Keyword = request.forms.get('query');
		notes = searchNotesFromUser(Keyword, sessionUser['UserID']);
		return template('notes', Keyword=Keyword, searchTemplate=True,  notes=notes, user=user);
	else:
		return redirectHome();

#####Create a note

@route('/create')
@route('/create/')
def createNoteForm():
	global sessionUser

	if (sessionUser == None):
		return template('login', user=None)

	note = {}
	colors = getColorsAvailable();
	return template('createNote', note=note, colors=colors, editNote=False, user=sessionUser)

""" Eliminate sql injection and other things like ' """
def cleanContent(content):
	content = str(request.forms.get('contentNote'));
	content = re.sub('[^a-zA-Z0-9 \n\.]', '', str(content)); # content wihtout special characters
	return content

def cleanTitle(title):
	cleanTitle = re.sub('[^a-zA-Z0-9 \n\.]', '', str(title)); # Title without special characters
	cleanTitle = cleanTitle.replace(' ', '-');
	return cleanTitle

def generatePermalink(title):
	randNumList = random.sample(range(1, 100), 4); #10 digits rand num
	randomNumber = ''.join(str(e) for e in randNumList);
	permalink = title + '-' + randomNumber;
	return permalink;

def getToday():
	today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	formatedToday = today.replace(" ", "-")
	formatedToday = formatedToday.replace(":", "-");
	return formatedToday

def createnewNote(api):
	global sessionUser

	errorNote = {
		# only for the api...
		"error"     : True,
		"message"   : "You're not allowed to do this...",
	}

	if (sessionUser == None):
		if (api):
			response.content_type = 'application/json';
			return json.dumps(errorNote);
		else:
			return template('login', user=None)

	title 	= cleanTitle(request.forms.get('titleNote'));
	content = cleanContent(request.forms.get('contentNote'));
	permalink = generatePermalink(title);
	today 	= getToday();
	color 	= request.forms.get('colorNote');
	private = int(request.forms.get('privateNote'));

	newNote = {
		# only for the api...
		"error"     : True,
		"message"   : "Note was not created successfully",

		"NoteID" 	: None,
		"UserID" 	: sessionUser['UserID'],
		"Title" 	: title,
		"Permalink" : permalink,
		"Content" 	: content,
		"CreatedAt" : today,
		"EditedAt" 	: today,
		"Published" : 1,
		"Private" 	: private,
		"Color" 	: color
	}

	if createNoteDB(newNote):
		if api:
			newNote['error'] = False;
			newNote['message'] = "Note created successfully"
			response.content_type = 'application/json';

			return json.dumps(newNote);
		else:
			return template('note-created', user=sessionUser);
			response.status = 303
			response.set_header('Location', '/'+ sessionUser['Username']);
	else:
		if api:
			response.content_type = 'application/json';
			return json.dumps(newNote);
		else:
			return template('createNote', note=newNote, colors=None, user=sessionUser, editNote=False)

@route('/api/notes/create', method="POST")
def getApiNotes():
	api = True;
	return createnewNote(api);

@route('/create', method="POST")
def createnewNoteAux():
	api = False;
	return createnewNote(api);

@route('/profile')
def userProfile():
	global sessionUser
	if (sessionUser == None):
		return template('login', user=None)

	user = getUserbyID(sessionUser['UserID']);
	notes = getNotesByUserID(sessionUser['UserID']);
 
	if user != None:
		return template("profile", user=user, notes=notes);
	else:
		return template("login", user=sessionUser);

@route('/profile/edit')
def showFormToEditUser():
	global sessionUser
	if (sessionUser == None):
		return template('login', user=None)

	user = getUserbyID(sessionUser['UserID']);

	if (user != None):
		return template("signup", user=user, editUser=True);
	else:
		return redirectHome();

@route('/profile/edit', method="POST")
def editSessionUser():
	global sessionUser
	if (sessionUser == None):
		return template('login', user=sessionUser)

	user = getUserbyID(sessionUser['UserID']);

	user['Name'] = request.forms.get('namesignup');
	user['Surname'] = request.forms.get('surnamesignup');
	user['Birthday'] = request.forms.get('birthdaysignup'); 
	user['City'] = request.forms.get('citysignup'); 
 
	if updateUser(user):
		notes = getNotesByUserID(user['UserID']);
		return template("profile", notes=notes, user=user);
	else:
		return template("profile", user=sessionUser);

@route('/update/<NoteID>', method="POST")
def saveUpdateDatabase(NoteID):
	global sessionUser
	if (sessionUser == None):
		return redirectHome();
	
	newTitle 		 = request.forms.get('titleNote');
	newContent 		 = request.forms.get('contentNote');
	updatedTime 	 = datetime.now().strftime('%Y-%m-%d %H:%M:%S');

	#Update fields for the note before inserting into database..
	note 			 = getNotebyNoteID(NoteID); #get note object from the previous note.
	note['Title'] 	 = newTitle;
	note['Content']  = newContent;
	note['EditedAt'] = updatedTime;
	note['Color']    = request.forms.get('colorNote');
	note['Private']    = request.forms.get('privateNote');

	if updatedBD(note): #update the note into the database.

		response.status = 303

		user = getUserbyID(note['UserID'])

		response.set_header('Location', '/'+user['Username']+'/'+note['Permalink']);
		return template('singleNote', note=note, user=user); #Show login screen
		return template('singleNote', note=note, user=user);
	else:
		#problems updating note.
		return template('error', user=sessionUser)

@route('/delete/<NoteID>')
def deleteNoteID(NoteID):
	global sessionUser;
	if (sessionUser == None):
		return template('login')

	note = getNotebyNoteID(NoteID);

	if (note == None): 
		return redirectHome(); # The note doesn't exist on our database 

	userID_note    = note['UserID'];
	userID_session = sessionUser['UserID'];

	if (userID_note == userID_session):
		if (deleteNote(NoteID)):
			return template('notes-deleted', user=sessionUser);
		else:
			return "Problems deleting that note<a href='/'>Go to your profile</a>"
			return template('error')
	else:
		return template('privateZone', user=sessionUser); # Private note. Guest can't read this note

@route('/api/notes/delete/<NoteID>', mehod="GET")
def deleteNoteID(NoteID):
	global sessionUser;

	response.content_type = 'application/json';
	returnedMessage = {
		"NoteID" : NoteID,
		"valid" : "false",
		"deleted": "false",
		"status" : "You're not allowed to do this action"
	}

	if (sessionUser == None):
		return json.dumps(returnedMessage);

	note = getNotebyNoteID(NoteID);

	if (note == None): 
		returnedMessage["deleted"] = "false";
		returnedMessage["status"]  = "This note doesn't exist on our system or has changed location";
		return json.dumps(returnedMessage); # The note doesn't exist on our database 

	userID_note    = note['UserID'];
	userID_session = sessionUser['UserID'];

	if (userID_note == userID_session):
		if (deleteNote(NoteID)):
			returnedMessage['valid'] = 'true';
			returnedMessage['deleted'] = "true";
			returnedMessage['status'] = "We have deleted your note!";
		else:
			returnedMessage['deleted'] = "false";
			returnedMessage['status'] = "You're not allowed to delete this note.";

	return json.dumps(returnedMessage);

	

#####Show a single 

@route('/<Username>#/<Permalink>')
@route('/<Username>/<Permalink>')
def displayNote(Username, Permalink):
	global sessionUser

	note = getNoteby_Username_Permalink(Username, Permalink);

	if (note == None):
		return "The note you're trying to read dont exist";
		return redirectHome(); # the note doesn't exist

	if sessionUser != None:	
		if int(note['Private']) == 0 or sessionUser['UserID'] == note['UserID']: #la NOTa es publica o el usuario esta conectado
			return template('singleNote', note=note, user=sessionUser);
		
	return template('privateZone', user=sessionUser); # Private note. Guest can't read this note

@route('/<Username>/<Permalink>/edit')
def updateNote(Username, Permalink):
	global sessionUser
	if sessionUser == None:
		return template('login', user=sessionUser)

	note = getNoteby_Username_Permalink(Username, Permalink);

	if note == None:
		return redirectHome();

	if sessionUser['UserID'] == note['UserID']:
		colors = getColorsAvailable(); # get all the available colors
		return template('createNote', note=note, colors=colors,user=sessionUser, editNote=True)
	
	return template('privateZone', user=sessionUser); # Private note. Guest can't read this note

@route('/api/notes/<NoteID:int>', method='GET')
@route('/api/notes/<NoteID:int>', method='POST')
def getNodeByID_api(NoteID):
	global sessionUser

	errorNote  = { "NoteID" : NoteID, "valid": "false", "status": "notExist"}
	note 	   = getNotebyNoteID(NoteID);

	response.content_type = 'application/json';

	if (note != None):
		if  note['Private'] == 0 or (note['Private'] == 1 and sessionUser['UserID'] == note['UserID']):
			# Is a public note or session user is the owner.
			note['valid'] = "true";
			note['status'] = "OK";
			return json.dumps(note); # return a not empty note.
		else:
			errorNote['valid'] = "false";
			errorNote['status'] = "You don't permissions to see this content. Sorry.";
	else:
		errorNote['valid'] = "false";
		errorNote['status'] = "The note you're trying to read doesn't exist or was removed.";

	return json.dumps(errorNote); # return error note.

	if (sessionUser['UserID'] != note['UserID']):
		errorNote['status'] = "You don't permissions to see this content. Sorry.";
		return json.dumps(errorNote);
	elif (note == None):
		errorNote['status'] = "The note you're trying to read doesn't exist or was removed.";
		return json.dumps(errorNote);
	else:
		# At this point the user is the correct one and the note is not None
		note['valid'] = "true";
		errorNote['status'] = "OK";
		response.content_type = 'application/json'
		return json.dumps(note);

#Show the profile for a given user. 
#Dashboard with the Published notes, draft and more stuff... """

@route('/<username>')
@route('/<username>/')
def profile(username):
	global sessionUser
	if (sessionUser == None):
		return template('login', user=None)

	user = getUserbyUsername(username);

	if user != None and user['UserID'] == sessionUser['UserID']: # if user and session is the same as the query user
		notes = getNotesByUserID(user['UserID']);
		return template('notes', searchTemplate=False, notes=notes, user=user); # Show the notes for that user!
	else:
		return template('prohibited_place', user=sessionUser)
	
run(host='127.0.0.1', port=3000);