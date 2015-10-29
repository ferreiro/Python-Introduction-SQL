import sqlite3

dbfile = "managmentSystem.sqlite3"

# t = table's name | f = filename
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
	apliedStudents = []

	# cursor.execute('Select * from Students where not in (Select Students.ID FROM Students, Aplications WHERE Students.ID=Aplications.ID)');
	for line in cursor: apliedStudents.append(line)

	cursor.execute('Select Students.ID FROM Students');

	for line in cursor:
		print line
 
	# JOIN Aplications ON Students.ID=Aplications.ID
firstQuery(cursor);
thirdQuery(cursor);

