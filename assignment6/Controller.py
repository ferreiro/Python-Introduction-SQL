import sqlite3
from bottle import request, route, run, template, response;
from datetime import datetime

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



#################################
############AUXILIAR FUNCTIONS #############
#################################

def setSessionUser(user):
	global sessionUser

	try:
		if (user != None):
			sessionUser = {
				"UserID" : user[0],
				"Email" : user[1],
				"Username" : user[3],
				"Name" : user[4],
				"Surname" : user[5],
				"Birthday" : user[6],
				"City" : user[7],
				"Premium" : user[8]
			}
			#print user;
			#print sessionUser;
	except:
		print "Can't set the user session"
		return False; # Coudln't set a session user

	return True; # set!

def validUser(user):
	return (user != None);

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

def getNotebyUserID_NoteID(UserID, NoteID):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes join User where User.UserID="+str(UserID)+" And Notes.NoteID="+str(NoteID);
		cursor.execute(query); # Check if the email and password exists on our database
		note = cursor.fetchone(); # Get the returned object for the database
		closeCursor(cursor);
	except:
		print "Can't get notes given a userID and NoteID"

	return note;


def getNotebyNoteID(NoteID):
	note   = None;
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.NoteID="+str(NoteID);
		cursor.execute(query); # Check if the email and password exists on our database
		noteTuple = cursor.fetchone(); # Get the returned object for the database
		note = notetupleToDictionary(noteTuple);
		print note;
		closeCursor(cursor);
	except:
		print "Can't get notes given a userID and NoteID"

	return note;

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

def getNoteIDFromPermalink(Permalink):
	noteID = -1;
	cursor = openCursor();
	try:
		query = "Select NoteID from Notes where Notes.Permalink='"+str(Permalink)+"'";
		print query
		cursor.execute(query); # Check if the email and password exists on our database
		noteID = cursor.fetchone()[0]; # Get the returned object for the database
		closeCursor(cursor);
	except:
		print "Can't retrieve a user"

	return noteID;


# FetchAll notes for a given user id
# Add all the notes returned by the query into a list

def validNotes(notes):
	return (notes != None);


# Convert a note as a tuple into a Dictionary and return it

def usertupleToDictionary(_tuple):
	if (type(_tuple) != tuple):
		return None;

	user = {}
	user['UserID'] = _tuple[0]
	user['Email'] = _tuple[1]
	user['Password'] = _tuple[2]
	user['Username'] = _tuple[3]
	user['Name'] = _tuple[4]
	user['Surname'] = _tuple[5]
	user['Birthday'] = _tuple[6]
	user['City'] = _tuple[7]
	user['Premium'] = _tuple[8]

	return user;

def notetupleToDictionary(_tuple):
	if (type(_tuple) != tuple):
		return None;
	note = {}
	note['NoteID'] 		= _tuple[0]
	note['UserID'] 		= _tuple[1]
	note['Title'] 		= _tuple[2]
	note['Permalink'] 	= _tuple[3]
	note['Content'] 	= _tuple[4]
	note['CreatedAt'] 	= _tuple[5]
	note['EditedAt'] 	= _tuple[6]
	note['Published']	= _tuple[7]
	note['Private'] 	= _tuple[8]

	return note;

def getUserNotes(UserID):
	notes_arr = []; # Array of dictionary (with notes)
	cursor = openCursor();
	try:
		query = "Select * from Notes where Notes.UserID=" + str(UserID);
		cursor.execute(query); # Check if the email and password exists on our database
		notes_tuples = cursor.fetchall(); # Get tuples returned by database
		
		# notes are tuples. So convert to dict and add to Notes array
		for n in notes_tuples:
			convertedNote = notetupleToDictionary(n); # tuple to dictionary
			notes_arr.append(convertedNote); # Append dictionary

		closeCursor(cursor);

	except:
		print "Can't retrieve a notes"

	return notes_arr;

""" Create a user in the database if the user doesn't exist """

def createUserDB(newUser):
	cursor = openCursor();

	try:
		userString  = ("NULL,");
		userString += ("'" + str(newUser['email']) + "',");
		userString += ("'" + str(newUser['password']) + "',");
		userString += ("'" + str(newUser['username']) + "',");
		userString += ("'" + str(newUser['name']) + "',");
		userString += ("'" + str(newUser['surname']) + "',");
		userString += ("'" + str(newUser['birthday']) + "',");
		userString += ("'" + str(newUser['city'])     + "',");
		userString += str(newUser['premium']);

		print userString

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
	print "Oh tes"
#try:
	userString  = ("NULL,");
	userString += str(newNote['UserID']) + ",";
	userString += ("'" + str(newNote['Title']) + "',");
	userString += ("'" + str(newNote['Permalink']) + "',");
	userString += ("'" + str(newNote['Content']) + "',");
	userString += ("'" + str(newNote['CreatedAt']) + "',");
	userString += ("'" + str(newNote['EditedAt']) + "',");
	userString += (str(newNote['Published']) + ",");
	userString += str(newNote['Private']);

	query = "Insert into Notes values(" + userString + ')';
	print query
	cursor.execute(query);
	conn.commit();
	closeCursor(cursor);

	return True;

#except:
	return False;

def updatedBD(updatedNote):
	cursor = openCursor();
	query  = "Update Notes SET "
	query += "Title ='" + str(updatedNote['Title']) + "',  ";
	query += "Content ='" + str(updatedNote['Content']) + "'";
	query += " where Notes.NoteID=" + str(updatedNote['NoteID']);
	query += " and Notes.UserID=" + str(updatedNote['UserID']);

	print query

	cursor.execute(query);
	conn.commit();
	closeCursor(cursor);

	return True; # Updated.

def deleteNote(NoteID):
	cursor = openCursor();
#try:
	query = "delete from Notes where notes.NoteID=" + str(NoteID) + ""
	cursor.execute(query);
	conn.commit();
	closeCursor(cursor);
	return True;
#except:
	#print "somethings go wrong"
	#return False;


#################################
############ROUTES #############
#################################

def redirectHome():
	response.status = 303
	response.set_header('Location', '/');
	return template('login'); #Show login screen

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
		return template('login'); #Show login screen
	else:
		return loginSuccessRedirect();

@route('/login', method='POST')
def login():
	global sessionUser

	try:
		email    = request.forms.get('email');
		password = request.forms.get('password');
		user = getUserbyEmailPassword(email, password);

		if validUser(user):
			setSessionUser(user); # set User session object
		else:
			return "The user is NOT valid!";
	except:
		print "Problems with your query. Sorry..."

	return loginSuccessRedirect();

######### Register 
@route('/register')
def register():
	global sessionUser
	if (sessionUser == None):
		return template('signup'); #Show login screen
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
		return template('signup-success');
	else:
		return "Problems creating user"

	print "Problems inserting a user on the database. Sorry..."
	return "Problems on the database"


#####Create a note

@route('/create')
@route('/create/')
def createNoteForm():
	note = {}
	return template('createNote', note=note, editNote=False)

@route('/create', method="POST")
def createNote():
	global sessionUser

	if (sessionUser == None):
		return template('login')

	title = request.forms.get('titleNote');
	today = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
	formatedToday = today.replace(" ", "-")
	formatedToday = formatedToday.replace(":", "-")
	permalink = str(title) + str(formatedToday);

	newNote = {
		"NoteID" 	: None,
		"UserID" 	: sessionUser['UserID'],
		"Title" 	: str(title),
		"Permalink" : str(permalink),
		"Content" 	: str(request.forms.get('contentNote')),
		"CreatedAt" : today,
		"EditedAt" 	: today,
		"Published" : 1,
		"Private" 	: 1
	}

	if createNoteDB(newNote):
		print "Note created!";
		response.status = 303
		response.set_header('Location', '/'+ sessionUser['Username'] + '/' + newNote['Permalink']);
		#return template('singleNote', note=newNote, user=sessionUser)
	else:
		return template('createNote', note=newNote, user=sessionUser, editNote=False)


@route('/update/<NoteID>', method="POST")
def saveUpdateDatabase(NoteID):
	if (sessionUser == None):
		return template('login')
	
	newTitle 		 = request.forms.get('titleNote');
	newContent 		 = request.forms.get('contentNote');
	updatedTime 	 = datetime.now().strftime('%Y-%m-%d %H:%M:%S');

	#Update fields for the note before inserting into database..
	note 			 = getNotebyNoteID(NoteID); #get note object from the previous note.
	note['Title'] 	 = newTitle;
	note['Content']  = newContent;
	note['EditedAt'] = updatedTime;

	user   = getUserbyID(note['UserID']);

	if updatedBD(note): #update the note into the database.
		return template('singleNote', note=note, user=user);
	else:
		#problems updating note.
		return template('error')

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
			return template('notes-deleted');
		else:
			return "Problems deleting that note"
			return template('error')
	else:
		redirectHome();
		return "You're not allowed to be here";


#####Show a single 

@route('/<Username>/<Permalink>')
def displayNote(Username, Permalink):
	global sessionUser
	if (sessionUser == None):
		return template('login')

	user = getUserbyUsername(Username);
	UserID = user['UserID'];
	NoteID = getNoteIDFromPermalink(Permalink);

	if (NoteID != 0):
		note_tuple = getNotebyUserID_NoteID(UserID, NoteID);
		note = notetupleToDictionary(note_tuple);
		return template('singleNote', note=note, user=sessionUser)
	else:
		# note no existe
		return template('loginWindow')

@route('/<Username>/<Permalink>/edit')
def updateNote(Username, Permalink):
	global sessionUser
	note = {}

	if (sessionUser == None):
		return template('login')

	user   = getUserbyUsername(Username);
	UserID = user['UserID'];
	NoteID = getNoteIDFromPermalink(Permalink);

	if (NoteID != 0):
		note_tuple = getNotebyUserID_NoteID(UserID, NoteID);
		note = notetupleToDictionary(note_tuple);
		return template('createNote', note=note, user=sessionUser, editNote=True)
	else:
		# note no existe
		return template('loginWindow')

#Show the profile for a given user. 
#Dashboard with the Published notes, draft and more stuff... """

@route('/<username>')
@route('/<username>/')
def profile(username):
	user = getUserbyUsername(username);
	if user != None:
		notes = getUserNotes(user['UserID']);
		return template('notes', notes=notes, user=user); # Show the notes for that user!
	else:
		return "User not exist"
	
run(host='127.0.0.1', port=3000);