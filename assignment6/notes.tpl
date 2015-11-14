% include ('header.tpl', title='Hola')
	
	
	<div class="Profile-Header-wrap">
		<div class="Profile-Header">
			<h1 class="Profile-Header-Name">
				my
				<strong>Notes</strong>
			</h1>
		</div>
	</div>

	<div class="containter-wrapper">
		<div class="containter">
				
			% if len(notes) == 0:
				<div class="Zero-NotesWrap">
					<div class="Zero-Notes">
						<h1 class="Zero-Notes-Title">Hi {{user['Name']}}!,<br /> You haven't written any note yet.</h1>
						<a class="Zero-Notes-Create" href="/create">Write your first Note now!</a>
					</div>
				</div>
				<div class="Note-wrapper">
					<div class="Note">

						<div class="Note-link">
							<a href="/create">
						</div>
						<a href="/create">+ Write your first Note now!</a>
					</div>
				</div>
			%else:
			% for note in notes:

				<div class="Note-wrapper">
					<div class="Note" id="{{note['NoteID']}}">

						<div class="Note-Options">
							<span class="Note-Options-link">
								+
							</span>
							<ul class="Note-Options-dropDown">
								<li><a href="/{{user['Username']}}/{{note['Permalink']}}/edit">
									Edit Note
								</a></li>
								<li><a href="/delete/{{note['NoteID']}}">
									Delete
								</a></li>
							</ul>
						</div>
						
						<div class="Note-line-color" style="background-color:#{{note['ColorHEX']}};"></div>

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

						<div class="Note-Metada">
							
							% if (note['Private']):
								<span class="Note-Private">
									<b>Private</b>
								</span>
							% else:
								<span class="Note-Private">
									<b>Public note (?)</b>
								</span>
							% end

							<span>-</span>

							% if (note['Published']):
								<span class="Note-Private">
									<b>Published on:</b>
									<% 
										date = note['CreatedAt']
										date = date.split(' ');
										date = date[0]
									%>
									{{date}}
								</span>
							% else:
								<span class="Note-Private">
									<b>Draft (?)</b>
								</span>
							% end
						</div>

					</div>
				</div>
				
			% end

		</div>
	</div>


% include ('footer.tpl')
