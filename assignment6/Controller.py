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

	data = cursor.fetchone();
	print data
	for c in cursor:
		print c

	if (data is None):
		print "Is none"
	else:
		print "The user is found"


	cursor.close()

	# if success create a cookie an redirect to notes/
	# else show an error on the login view.
		#return template('login', );
	return "<h1>Hola</h1>"

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





