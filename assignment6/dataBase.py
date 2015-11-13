import sqlite3

conn   = sqlite3.connect('notes.sqlite3')
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()

def createTableList(cursor):
	SQLtables = []

	UserTable = """
		create table User(
			UserID integer PRIMARY KEY AUTOINCREMENT,
			Email text UNIQUE,
			Password text,
			Username text UNIQUE,
			Name text,
			Surname text,
			Birthday date,
			City text
		)
	"""
	SQLtables.append(UserTable);

	notesTable = """
		create table Notes(
			NoteID integer PRIMARY KEY AUTOINCREMENT,
			UserID integer,
			Title text,
			Permalink text UNIQUE,
			Content text,
			CreatedAt date,
			EditedAt date,
			Published boolean,
			Private boolean,

			foreign key (UserID) references User ON DELETE CASCADE
		)
	"""
	SQLtables.append(notesTable);

	tagTable = """
		create table Tag(
			TagNameID text,
			NoteID integer,
			UserID integer,
			Color text,

			constraint Tag_user primary key(TagNameID, UserID), 
			foreign key(NoteID) references Notes ON DELETE CASCADE,
			foreign key(UserID) references User ON DELETE CASCADE
		)
	"""
	SQLtables.append(tagTable);

	return SQLtables;
	#cursor.execute("DROP TABLE IF EXISTS Notes")
	#cursor.execute("DROP TABLE IF EXISTS University")
	#cursor.execute("CREATE TABLE University(Nombre_Univ TEXT, Comunidad TEXT, Plazas INTEGER, PRIMARY KEY(Nombre_Univ))")

def deleteDatabase(cursor):
	cursor.execute("DROP TABLE IF EXISTS User ");
	cursor.execute("DROP TABLE IF EXISTS Tag");
	cursor.execute("DROP TABLE IF EXISTS Notes");

def createDatabase(cursor, tables):
	deleteDatabase(cursor);
	for t in tables:
		#print t
		cursor.execute(t);
		
tables = createTableList(cursor);
createDatabase(cursor, tables);

cursor.execute("insert into User values (NULL,'jgfe@hola.es', '123', 'ferreiro', 'Jorge', 'Garcia', '16/03/1995', 'Madrid')");
cursor.execute("insert into Notes values (NULL, 1, 'How to make pizza', 'how-make-pizza','So. We have to call Luigi.', '16/03/1995', '16/03/1995', 1, 0)");
cursor.execute("insert into Tag values ('Hello', 1, 1, '000000')");

cursor.execute("insert into User values (NULL,'test@example.com', '123', 'tomasso', 'Tommaso', 'Innocenti', '30/09/1991', 'Arezzo')");
cursor.execute("insert into Notes values (NULL, 2, 'How to make pasta','how-make-pasta' ,'So. We have to call Luigi.', '16/03/2015', '16/03/2020', 1, 0)");
cursor.execute("insert into Tag values ('Hello', 2, 2, '000000')");

cursor.execute("insert into User values (NULL,'test1@example.com', '123', 'paco', 'Paco', 'Innocenti', '30/09/1991', 'Arezzo')");
cursor.execute("insert into User values (NULL,'test2@example.com', '123', 'susana', 'Susana', 'Innocenti', '30/09/1991', 'Arezzo')");

#cursor.execute("Select * from Tag where Tag.UserID=1 and Tag.TagNameID='Hello'");
#cursor.execute("Select * from User where User.UserID=1");
#cursor.execute("Select DISTINCT Email from Tag join User on Tag.TagNameID='Hello' ");
#cursor.execute("Select DISTINCT Email from Tag join User on Tag.TagNameID='Hello' ");

#for t in cursor:
#	print t;

conn.commit()
cursor.close()