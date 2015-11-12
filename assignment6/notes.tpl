
% for i in user:
<p> {{i}}</p>
% end

% for note in notes:
	<p> {{note['Title']}}</p>
	<p> {{note['Content']}}</p>
	<p> {{note['CreatedAt']}}</p>
	<p> {{note['EditedAt']}}</p>
	<p> {{note['Published']}}</p>
	<p> {{note['Private']}}</p>
% end