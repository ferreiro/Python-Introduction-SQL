
% for i in user:
<p> {{i}}</p>
% end

<p>if the user is logged (check the cookies) Show the notes</p>

% if len(notes) == 0:
	<h2>Empty. There's any Note here</h2>
%end
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
		<h1 class="Note-Title">
			{{note['Title']}}
		</h1>
		<p class="Note-Content">
			{{note['Content']}}
		</p>
		<p> {{note['EditedAt']}}</p>
		<p> {{note['Published']}}</p>
		<p> {{note['Private']}}</p>
	</div>
	
% end
<p>Not logged? Check if the note is private or not</p>
	<p>Private? Show an error on the screen</p>
	<p>Not Private? Display the note</p>
