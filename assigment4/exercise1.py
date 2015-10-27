import sqlite3

conn   = sqlite3.connect('managmentSystem.sqlite3')
cursor = conn.cursor()

def createUniversityTable(cursor):
	cursor.execute("DROP TABLE IF EXISTS University")
	cursor.execute("CREATE TABLE University(universityName TEXT, community TEXT, max_capacity INTEGER, PRIMARY KEY(universityName))")

def createStudentTable(cursor):
	cursor.execute("DROP TABLE IF EXISTS Students")
	cursor.execute("CREATE TABLE Students(studentID TEXT, name TEXT, grade REAL, correction_value INT, PRIMARY KEY(studentID))")
	
def createApplicationsTable(cursor):
	cursor.execute("DROP TABLE IF EXISTS Aplications");
	cursor.execute("CREATE TABLE Aplications(studentID TEXT, universityName TEXT, degree TEXT, decition TEXT, PRIMARY KEY(universityName, studentID, degree), FOREIGN KEY(universityName) REFERENCES University(niversityName), FOREIGN KEY(studentID) REFERENCES Students(studentID))");

def createDatabase(cursor):
	createUniversityTable(cursor)
	createStudentTable(cursor)
	createApplicationsTable(cursor)
	return 0

createDatabase(cursor)
cursor.close()
conn.commit()

