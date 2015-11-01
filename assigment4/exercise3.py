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

def secondQuery(cursor):
	try:
		cursor.execute('Select Nombre_Est, Nota, Valor FROM Students')
		lineList = [] #List of student that have (nota-(nota*valor/1000))>1 

		for line in cursor:
			if (abs(line[1]-(line[1]*line[2])/1000)>1):
				#print line[0]+ str(line[1])+ str(line[2])
				lineList.append(line[0])
		print "Second query completed successfully...[OK]"

	except:
		print "Second query: database was previously updated with this data... [NOT INSERTED]"

def thirdQuery(cursor):
	noApliedStudents = []

	try:
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
		
		conn.commit()
		print "Third query completed successfully...[OK]"

	except:
		print "Third query: database was previously updated with this data... [NOT INSERTED]"

def fourthQuery(cursor):
	aplications = []

	try:
		#Devolver todos los estudiantes que querian estudiar economicas pero que no fueron admitidos en la unviersidad
		cursor.execute("SELECT * FROM Aplications WHERE Aplications.Decision='No' AND Aplications.Carrera = 'Economia' ");

		for entry in cursor:
			newAplication = []
			newAplication.append(entry[0]); #ID
			newAplication.append("Universidad de Jaen"); #Name
			newAplication.append("Economia"); #Carrera
			newAplication.append("Si"); #Insert also the decition for the aplications
			aplications.append(newAplication);

		#Insertar nuevas entradas admitiendoles en la universidad de jaen	
		for row in aplications:
			cursor.execute("INSERT INTO Aplications values (?, ?,?,?) ", (row[0], row[1], row[2], row[3]) );
		
		print "Fourth query completed successfully...[OK]"

	except:
		print "Fourth query: database was previously updated with this data... [NOT INSERTED]"

"""Borrar a todos los estudiantes que solicitaron mas de 2 carreras diferentes."""

def fithQuery(cursor):
	#idea find all id of student and for all student search on the aplication tabla and obtain only the carrera
	#if the Distincs carrera for each student is more than 2 borra ello
	aplications = []
	try:
		cursor.execute('Select ID FROM Students')
		lineList =[] #list of all id of students
		for line in cursor:
			lineList.append(line[0])
#find a way to pass the id of the student that are in lineList to serch for all the student
		for line in lineList:
			i=0
			cursor.execute("SELECT DISTINCT Carrera FROM Aplications WHERE Aplications.ID= %s",lineList[i]) 
			#cursor.execute("SELECT DISTINCT Carrera FROM Aplications WHERE Aplications.ID='345'") 
			for line in cursor:
				aplications.append(line[0])
				print str(line[0])

			if(len(aplications)>2):
				print str(len(aplications))
				#Student that have request more than 2 different carreras
				cursor.execute("DELETE From Aplications WHERE Aplications.ID='lineList[i]'")
				#cursor.execute("DELETE From Aplications WHERE Aplications.ID='345'")
				print "cancel from database"
				conn.commit()
			i=+1

		#cursor.execute('Select ID,Nombre_Univ,Carrera,Decision FROM Aplications')
		#print "last query result:"
		#for line in cursor:
		#	print str(line[0]) + ", " + line[1]+ ", " + line[2]+ ", " + line[3]

		print "Fith query completed successfully...[OK]"

	except:
		print "Fith query: database was previously updated with this data... [NOT INSERTED]"



#firstQuery(cursor);
#secondQuery(cursor)
#thirdQuery(cursor);
#fourthQuery(cursor);
fithQuery(cursor);

conn.commit()
cursor.close()

