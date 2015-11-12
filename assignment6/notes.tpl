
% for i in user:
<p> {{i}}</p>
% end

<p>if the user is logged (check the cookies) Show the notes</p>

% if len(notes) == 0:
	<p>OMG</p>
%end
% for note in notes:
	<p> {{note['Title']}}</p>
	<p> {{note['Content']}}</p>
	<p> {{note['CreatedAt']}}</p>
	<p> {{note['EditedAt']}}</p>
	<p> {{note['Published']}}</p>
	<p> {{note['Private']}}</p>
% end
<p>Not logged? Check if the note is private or not</p>
	<p>Private? Show an error on the screen</p>
	<p>Not Private? Display the note</p>
