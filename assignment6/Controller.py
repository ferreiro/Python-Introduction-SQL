import sqlite3
from bottle import request, route, run, template, response;

dbfile = "notes.sqlite3"

# DB configuration
def config(dbfile):
	conn   = sqlite3.connect(dbfile)
	cursor = conn.cursor()
	return conn, cursor

config = config(dbfile);
conn   = config[0]
cursor = config[1]

# DB configuration
def connectDB():
	global cursor
	return cursor

currentUserID = None; # change this to COOOKIES

@route('/')
@route('/login')
def login():
	return template('login')

@route('/register')
def displayRegisterPage():
	return template('register');

@route('/register', method='POST')
def registerUser():

	print request.forms.get('namesignup');
	user = {
		"email" : request.forms.get('emailsignup'),
		"password" : request.forms.get('passwordsignup'),
		"name": request.forms.get('namesignup'),
		"surname": request.forms.get('surnamesignup'),
		"birthday": request.forms.get('birthdaysignup'),
		"city": request.forms.get('citysignup')
	}

	print user;

	query 	 = "Select * from User where User.Email='"+str(user['email'])+"' And User.Password='"+str(user['password']) + "'";
	


	return "Your're now registered";

# Check if the user exists on the database if not. Returns a false error to the view.
@route('/login', method='POST')
def checkUser():
	global currentUserID;

	email 	 = request.forms.get('email');
	password = request.forms.get('password');
	query 	 = "Select * from User where User.Email='"+str(email)+"' And User.Password='"+str(password) + "'";
	
	cursor.execute(query);
	user = cursor.fetchone();

	if (user is None):
		# if success create a cookie an redirect to notes/
		return "<h1>User wasn't found</h1>"
		return template('login', loginError=True);
	else:
		userID = user[0];


		currentUserID = userID; # delete when cookies are added


		getNotes(userID);
		# else show an error on the login view.
		print "The user is found"
		
		response.status = 303
		response.set_header('Location', '/notes')

		#return getNotes(userID):
		#return template('notes', user=user);
		
@route('/<userID>/notes')
def getNotes(userID):

	# FetchAll notes for a given user id
	# Add all the notes returned by the query into a list

	try:
		query  = "Select * from Notes where Notes.UserID='" + str(userID) + "'"; 
		cursor.execute(query);

		notes = [] # list of nodes for a given user ID

		for c in cursor.fetchall():
			singleNote = {}
			singleNote['NoteID'] 	= c[0]
			singleNote['UserID'] 	= c[1]
			singleNote['Title'] 	= c[2]
			singleNote['Content'] 	= c[3]
			singleNote['CreatedAt'] = c[4]
			singleNote['EditedAt'] 	= c[5]
			singleNote['Published'] = c[6]
			singleNote['Private'] 	= c[7]
			
			notes.append(singleNote); # Add the note to the Notes.

		return template('notes', notes=notes, user= {'Hola'});# return notes to the template.

	except:
		return template('error')

@route('/notes')
def showNotes():
	global currentUserID  # delete when cookies are added
	return getNotes(currentUserID); # pass the logged user ID


def checkSession():
	# if user is not register. Redirect to Home
	print "Hola"

def closeDB(conn, cursor):
	conn.commit() # Update changes to database
	cursor.close()

run(host='127.0.0.1', port=3000);





