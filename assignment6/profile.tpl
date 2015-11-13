% include ('header.tpl', title='Hola')

	This is my profile :-)

	<p>Name: {{user['Name']}}</p>
	<p>Surname: {{user['Surname']}}</p>
	<p>Username: {{user['Username']}}</p>
	<p>Email: {{user['Email']}}</p>
	<p>Birthday: {{user['Birthday']}}</p>
	<p>City: {{user['City']}}</p>
	<p>Premium: {{user['Premium']}}</p> 

% include ('footer.tpl')