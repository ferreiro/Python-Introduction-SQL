% include ('header.tpl', title='Hola')

	<p>if the user is logged (check the cookies) Show the notes</p>

	<form action="/search" method="POST">
		<p> 
			<label for="searchText" class="uname" data-icon="u">Search title or content</label>
			<input id="searchText" name="query" required="required" type="text" placeholder="Search by title or content..." /> 
		</p>
	</form>


	% if len(notes) == 0:
		<h2>Empty. There's any Note here</h2>
	%else:
	% for note in notes:

		<div class="Note" id="{{note['NoteID']}}">

			% if (note['Private']):
				<span class="Note-Private">
					<b>Private Note</b>
				</span>
			% end
			<h3 class="Note-Title">
				{{note['CreatedAt']}}
			</h3>

			<p>
				<a href="/{{user['Username']}}/{{note['Permalink']}}/edit">Edit note</a>
			</p>
			<p><a href="/delete/{{note['NoteID']}}">Delete note</a></p>


			<h1 class="Note-Title">
				<a href="/{{user['Username']}}/{{note['Permalink']}}">
					{{note['Title']}}
				</a>
			</h1>
			<p class="Note-Content">
				{{note['Content']}}
			</p>
			<p> {{note['Published']}}</p>
			<p> {{note['Private']}}</p>
		</div>
		
	% end

	<p>Not logged? Check if the note is private or not</p>
		<p>Private? Show an error on the screen</p>
		<p>Not Private? Display the note</p>



% include ('footer.tpl')
