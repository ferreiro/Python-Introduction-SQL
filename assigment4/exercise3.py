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

	print "First query result:"
	for line in cursor:
		print line[0] + ", " + str(line[1]) + ", " + line[2]

def thirdQuery(cursor):
	noApliedStudents = []

	sqlquery = """SELECT * FROM Students WHERE Students.ID not IN \
	              (Select Students.ID FROM Students JOIN Aplications WHERE Students.ID=Aplications.ID)"""

	cursor.execute(sqlquery); # Execute the query in order to get in cursor all the students that id doesn't appear on the aplications table
	
	for line in cursor:
		lineList = []
		lineList.append(line[0]); #ID
		lineList.append("Universidad de Jaen"); #Name
		lineList.append("Informatica"); #Carrera
		lineList.append("Si"); #Insert also the decition for the aplications 
		#lineList.append(line[2]); #nota media
		noApliedStudents.append(tuple(lineList));

	for entry in noApliedStudents:
		cursor.execute("INSERT INTO Aplications values (?, ?,?,?) ", (entry[0], entry[1], entry[2], entry[3]) );
	
	print "Third query complete successfully...[OK]"
	conn.commit()

def fourthQuery(cursor):
	aplications = []

	#Devolver todos los estudiantes que querian estudiar economicas pero que no fueron admitidos en la unviersidad
	cursor.execute("SELECT * FROM Aplications WHERE Aplications.Decision='No' AND Aplications.Carrera = 'Economia' ");

	for entry in cursor:
		newAplication = []
		newAplication.append(entry[0]); #ID
		newAplication.append("Universidad de Jaen"); #Name
		newAplication.append("Economia"); #Carrera
		newAplication.append("Si"); #Insert also the decition for the aplications
		aplications.append(newAplication);
	
	for row in aplications:
		cursor.execute("INSERT INTO Aplications values (?, ?,?,?) ", (row[0], row[1], row[2], row[3]) );

	#Insertar nuevas entradas admitiendoles en la universidad de jaen
	print "TODO"

#firstQuery(cursor);
#firstQuery(cursor);
#thirdQuery(cursor);
fourthQuery(cursor);

conn.commit()
cursor.close()

