import sqlite3

dbfile = "managmentSystem.sqlite3"

#t = table's name | f = filename
t_university    = "University"
f_university    = "./dbFiles/universities.txt"
t_students      = "Students"
f_students      = "./dbFiles/students.txt"
t_aplications   = "Aplications"
f_aplications   = "./dbFiles/solicitudes.txt"

# DB configuration
def config(dbfile):
	conn   = sqlite3.connect(dbfile)
	cursor = conn.cursor()
	return conn, cursor

config = config(dbfile);
conn   = config[0]
cursor = config[1]

def firstQuery(cursor):
	#cursor.execute('Select * From Students JOIN Aplications ON Students.ID=Aplications.ID WHERE Students.Valor<1000 AND Aplications.Nombre_Univ="Universidad Complutense de Madrid" AND Aplications.Carrera="Informatica" AND Aplications.Decision="Si"')
	cursor.execute('Select Nombre_Est, Nota, Decision FROM Students JOIN Aplications ON Students.ID=Aplications.ID WHERE Students.Valor<1000 AND Aplications.Nombre_Univ="Universidad Complutense de Madrid" AND Aplications.Carrera="Informatica"')

	for line in cursor:
		print line[0] + ", " + str(line[1]) + ", " + line[2]

def thirdQuery(cursor):
	noApliedStudents = []

	sqlquery = """SELECT * FROM Students WHERE Students.ID not IN \
	              (Select Students.ID FROM Students JOIN Aplications WHERE Students.ID=Aplications.ID)"""

	cursor.execute(sqlquery);
	
	for line in cursor:
		lineList = []
		lineList.append(line[0]); #ID
		lineList.append("Universidad de Arizona"); #Name
		lineList.append("Informatica"); #Carrera
		lineList.append("Si"); #Insert also the decition for the aplications 
		#lineList.append(line[2]); #nota media
		noApliedStudents.append(tuple(lineList));

	for entry in noApliedStudents:
		#print str(entry)
		cursor.execute("INSERT INTO Aplications values (?, ?,?,?) ", (entry[0], entry[1], entry[2], entry[3]) );
		#insertQuery = "INSERT INTO Aplications values " + str(tuple(entry))
		#cursor.execute(insertQuery);
	
	print "thirdQuery complete successfully"
	conn.commit()

	#JOIN Aplications ON Students.ID=Aplications.ID
#firstQuery(cursor);
thirdQuery(cursor);

conn.commit()
cursor.close()

