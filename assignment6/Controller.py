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
		return template('login', );
	return template();

@route('notes')
def showNotes():
	# TODO: check if the user exists
	# Get all notes for that user. 
	# pass list of Notes to the view.

closeDB(conn, cursor)
run(host='127.0.0.1', port=3000);





