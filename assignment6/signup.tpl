<h1>Register page</h1>

<form action="/register" method="POST"> 
	<h1> Sign up </h1> 
	<p> 
		<label for="namesignup" class="uname" data-icon="u">Your name</label>
		<input id="namesignup" name="namesignup" required="required" type="text" placeholder="mysuperusername690" />
	</p>
	<p> 
		<label for="surnamesignup" class="usurname" data-icon="u">Your surname</label>
		<input id="surnamesignup" name="surnamesignup" required="required" type="text" placeholder="mysuperusername690" />
	</p>
	<p> 
		<label for="usernamesignup" class="username" data-icon="u">Your username</label>
		<input id="usernamesignup" name="usernamesignup" required="required" type="text" placeholder="mysuperusername690" />
	</p>
	<p> 
		<label for="birthdaysignup" class="ubirthday" data-icon="u">Your birthday</label>
		<input id="birthdaysignup" name="birthdaysignup" required="required" type="date"/>
	</p>
	<p> 
		<label for="citysignup" class="ucity" data-icon="u">Your city</label>
		<input id="citysignup" name="citysignup" required="required" type="name"/>
	</p>
	<p> 
		<label for="emailsignup" class="youmail" data-icon="e" > Your email</label>
		<input id="emailsignup" name="emailsignup" required="required" type="email" placeholder="mysupermail@mail.com"/> 
	</p>
	<p> 
		<label for="passwordsignup" class="youpasswd" data-icon="p">Your password </label>
		<input id="passwordsignup" name="passwordsignup" required="required" type="password" placeholder="eg. X8df!90EO"/>
	</p>
	<p class="signin button"> 
		<input type="submit" value="Sign up"/> 
	</p>
	<p class="change_link">  
		Already a member ?
		<a href="/login" class="to_register"> Go and log in </a>
	</p>
</form>