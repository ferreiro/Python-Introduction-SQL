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

def closeDB(conn, cursor):
	conn.commit() # Update changes to database
	cursor.close()


@route('/')
def login():
	return template('login')

# Check if the user exists on the database if not. Returns a false error to the view.
@route('/login', method='POST')
def checkUser():
	
	email = request.forms.get('email');
	password = request.forms.get('password');

	#cursor.execute("Select DISTINCT Email from Tag join User on Tag.TagNameID='Hello' ");

	#for t in cursor:
	#	print t;

	# if success create a cookie an redirect to notes/
	# else show an error on the login view.
	return template('login', loginError=True);
	return template();

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

closeDB(conn, cursor)
run(host='127.0.0.1', port=3000);





