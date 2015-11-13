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





cursor.execute(query);
conn.commit();
closeCursor(cursor);