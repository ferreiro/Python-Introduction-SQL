import sqlite3
from bottle import request, route, run, template;

dbfile = "notes.sqlite3"

# DB configuration
def config(dbfile):
	conn   = sqlite3.connect(dbfile)
	cursor = conn.cursor()
	return conn, cursor

config = config(dbfile);
conn   = config[0]
cursor = config[1]

@route('/')
def login():
	return template('login')

# Check if the user exists on the database if not. Returns a false error to the view.
@route('/login', method='POST')
def checkUser():
	global dbfile
	conn   = sqlite3.connect(dbfile)
	cursor = conn.cursor()

	email = request.forms.get('email');
	password = request.forms.get('password');

	query = "Select * from User where User.Email='"+str(email)+"' And User.Password='"+str(password) + "'";
	print query;
	
	cursor.execute(query);

	user = cursor.fetchone();

	cursor.close()

	if (user is None):
		# if success create a cookie an redirect to notes/
		print "Is none"
		return "<h1>User wasn't found</h1>"
		return template('login', loginError=True);
	else:
		# else show an error on the login view.
		print "The user is found"
		print user
		print type(user)
		return template('notes', user=user);
		return "yeahs"
		
	


@route('/<userID>/notes')
def showNotes(userID):
	userID = request.forms.get('userID');
	
	# FetchAll notes for a given user id
	# Add all the notes returned by the query into a list
	# return notes to the template.
	return "<h1>Hola</h1>";

@route('/notes/<id>')
def showNotes(id):

	note = {} # dictionary with information for a given note
	noteId = id; # id is passed by parameter on the url
	
	#Search note ID on the database.
	#if exits. Make a dictionary with the data: 


	return template('notes', note=note);

@route('notes')
def showNotes():
	# TODO: check if the user exists
	# Get all notes for that user. 
	# pass list of Notes to the view.
	print "hola"


def closeDB(conn, cursor):
	conn.commit() # Update changes to database
	cursor.close()

run(host='127.0.0.1', port=3000);





