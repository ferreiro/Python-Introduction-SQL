% include ('header.tpl', title='Hola')
	
	<div class="containter-wrapper">
		<div class="containter">
				
			% if len(notes) == 0:
				<div class="Zero-NotesWrap">
					<div class="Zero-Notes">
						<h1 class="Zero-Notes-Title">Hi {{user['Name']}}!,<br /> You haven't written any note yet.</h1>
						<a class="Zero-Notes-Create" href="/create">Write your first Note now!</a>
					</div>
				</div>
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

		</div>
	</div>


% include ('footer.tpl')
