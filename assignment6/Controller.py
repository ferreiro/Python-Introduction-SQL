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

	table = "User"

	print request.forms.get('namesignup');
	user = {
		"name": request.forms.get('namesignup'),
		"surname": request.forms.get('surnamesignup'),
		"username": request.forms.get('usernamesignup'),
		"birthday": request.forms.get('birthdaysignup'),
		"city": request.forms.get('citysignup'),
		"email" : request.forms.get('emailsignup'),
		"password" : request.forms.get('passwordsignup')
	}

	"""Take dictionary object dict and produce sql for 
	    inserting it into the named table"""
	
	userValue  = ("NULL,");
	userValue += ("'" + str(user['email']) + "',");
	userValue += ("'" + str(user['password']) + "',");
	userValue += ("'" + str(user['username']) + "',");
	userValue += ("'" + str(user['name']) + "',");
	userValue += ("'" + str(user['surname']) + "',");
	userValue += ("'" + str(user['birthday']) + "',");
	userValue += ("'" + str(user['city']) + "'");

	query = "Insert into User values(" + userValue + ')';
	print query
	cursor.execute(query);
	conn.commit()
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
		username = user[3];
		print userID
		print username


		currentUserID = userID; # delete when cookies are added


		getAllNotes(username);
		# else show an error on the login view.
		print "The user is found"
		
		response.status = 303
		response.set_header('Location', '/'+str(username));

		#return getNotes(userID):
		#return template('notes', user=user);

@route('/<username>')
@route('/<username>/')
def getAllNotes(username):

	# FetchAll notes for a given user id
	# Add all the notes returned by the query into a list

	try:
		query  = "Select * from Notes join User where User.Username='" + str(username) + "'"; 
		cursor.execute(query);

		notes = [] # list of nodes for a given user ID

		for c in cursor.fetchall():
			print c
			singleNote = {}
			singleNote['NoteID'] 	= c[0]
			singleNote['UserID'] 	= c[1]
			singleNote['Title'] 	= c[2]
			singleNote['Permalink'] = c[3]
			singleNote['Content'] 	= c[4]
			singleNote['CreatedAt'] = c[5]
			singleNote['EditedAt'] 	= c[6]
			singleNote['Published'] = c[7]
			singleNote['Private'] 	= c[8]
			
			notes.append(singleNote); # Add the note to the Notes.

		return template('notes', notes=notes, user= {'Hola'});# return notes to the template.

	except:
		return template('error')

@route('/<username>/<note_permalink>')
def getSingleNote(username, note_permalink):

	# FetchAll notes for a given user id
	# Add all the notes returned by the query into a list

	try:
		query  = "Select * from Notes join User where User.Username='" + str(username) + "' and Notes.Permalink='" + str(note_permalink) + "'"; 
		print query
		cursor.execute(query);

		notes = [] # list of nodes for a given user ID

		for c in cursor.fetchall():
			singleNote = {}
			singleNote['NoteID'] 	= c[0]
			singleNote['UserID'] 	= c[1]
			singleNote['Title'] 	= c[2]
			singleNote['Permalink'] = c[3]
			singleNote['Content'] 	= c[4]
			singleNote['CreatedAt'] = c[5]
			singleNote['EditedAt'] 	= c[6]
			singleNote['Published'] = c[7]
			singleNote['Private'] 	= c[8]
			
			notes.append(singleNote); # Add the note to the Notes.

		return template('singleNote', notes=notes, user= {'Hola'});# return notes to the template.

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





