import sqlite3

conn   = sqlite3.connect('noteProject.sqlite3')
cursor = conn.cursor()

def createTableList(cursor):
	SQLtables = []

	newTable = """
		create table User(
			
		)
	"""
	SQLtables.append(newTable);


	newTable = """
		create table Notes(
			NoteID integer PRIMARY KEY AUTOINCREMENT,
			UserID integer,
			Title text,
			Content text,
			BackgroundColor text,
			CreatedAt text,
			EditedAt text,
			status text,

			foreign key (UserID) references
		)
	"""
	SQLtables.append(newTable);

	newTable = """
		create table Tags(
			
		)
	"""

	SQLtables.append(newTable);

	return SQLtables;
	#cursor.execute("DROP TABLE IF EXISTS Notes")
	#cursor.execute("DROP TABLE IF EXISTS University")
	#cursor.execute("CREATE TABLE University(Nombre_Univ TEXT, Comunidad TEXT, Plazas INTEGER, PRIMARY KEY(Nombre_Univ))")

def deleteDatabase(cursor):
	cursor.execute("DROP TABLE IF EXISTS Notes");
	cursor.execute("DROP TABLE IF EXISTS Tags");

def createDatabase(cursor, tables):
	deleteDatabase(cursor);
	for t in tables:
		print t
		cursor.execute(t);
		
tables = createTableList(cursor);
createDatabase(cursor, tables);

cursor.execute("Insert into Notes(Title, Content) values ('Hola que tal', 'Me llamo jorge')");

conn.commit()
cursor.close()