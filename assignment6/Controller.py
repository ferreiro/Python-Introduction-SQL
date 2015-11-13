import sqlite3
from bottle import request, route, run, template, response;

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
				"City" : user[7]
			}
			#print user;
			#print sessionUser;
	except:
		print "Can't set the user session"
		return False; # Coudln't set a session user

	return True; # set!

def validUser(user):
	return (user != None);

def getUser(email, password):
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

# FetchAll notes for a given user id
# Add all the notes returned by the query into a list

def validNotes(notes):
	return (notes != None);

def getUserNotes(UserID):
	notes_arr = []; # Array of dictionary (with notes)
	cursor = openCursor();
	print UserID
	try:
		query = "Select * from Notes where Notes.UserID='" + str(UserID) + "'";
		print query
		cursor.execute(query); # Check if the email and password exists on our database
		notes_tuples = cursor.fetchall(); # Get tuples returned by database
		
		# notes are tuples. So convert to dict and add to Notes array
		for n in notes_tuples:
			print n
			convertedNote = tupleToDictionary(n); # tuple to dictionary
			notes_arr.append(convertedNote); # Append dictionary
		
		closeCursor(cursor);

	except:
		print "Can't retrieve a notes"

	return notes_arr;

""" Convert a note as a tuple into a Dictionary and return it """

def tupleToDictionary(_tuple):
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

#################################
############ROUTES #############
#################################

@route('/login')
def loginWindow():
	return template('login');

@route('/login', method='POST')
def login():
	global sessionUser

	try:
		email    = request.forms.get('email');
		password = request.forms.get('password');
		user = getUser(email, password);

		if validUser(user):
			setSessionUser(user); # set User session object
		else:
			return "The user is NOT valid!";

	except:
		print "Problems with your query. Sorry..."
	
	notes_arr = getUserNotes(sessionUser['UserID'])
	return template('notes', notes=notes_arr); # Show the notes for that user!

run(host='127.0.0.1', port=3000);