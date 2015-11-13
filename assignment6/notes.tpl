% include ('header.tpl', title='Hola')
	
	<div class="containter-wrapper">
		<div class="containter">
					
			<li class="Header-options-menu-button">
				<a href="/profile">My notes</a>
			</li>
			<li class="Header-options-menu-button">
				<a href="/profile">Profile</a>
			</li>
			<li class="Header-options-menu-button">
				<a href="/profile/edit">Edit profile</a>
			</li>
			<li class="Header-options-menu-button">
				<a href="/logout">Log out</a>
			</li>


			<p>if the user is logged (check the cookies) Show the notes</p>



			% if len(notes) == 0:
				<h2>Empty. There's any Note here</h2>
			%else:
			% for note in notes:

				<div class="Note-wrapper" id="{{note['NoteID']}}">
					<div class="Note">
						
						<div class="Note-link">
							<a href="/{{user['Username']}}/{{note['Permalink']}}">
						</div>

						<h1 class="Note-Title">
							{{note['Title']}}	
						</h1>
						<p class="Note-Content">
							<%
								data = note['Content'];
								data = data[:120] + '...'
								print data
							%>
							{{data}} 
						</p>
						<h3 class="Note-Date">
							<% 
								date = note['CreatedAt']
								date = date.split(' ');
								date = date[0]
							%>
							{{date}}
						</h3>

						% if (note['Private']):
							<span class="Note-Private">
								<b>Private Note</b>
							</span>
						% end

						<p>
							<a href="/{{user['Username']}}/{{note['Permalink']}}/edit">Edit note</a>
						</p>
						<p><a href="/delete/{{note['NoteID']}}">Delete note</a></p>


						<p> {{note['Published']}}</p>
						<p> {{note['Private']}}</p>
					</div>
				</div>
				
			% end

			<p>Not logged? Check if the note is private or not</p>
				<p>Private? Show an error on the screen</p>
				<p>Not Private? Display the note</p>


		</div>
	</div>


% include ('footer.tpl')
