% include ('header.tpl', title='Hola')


<div class="Profile-Header-wrap">
	<div class="Profile-Header">
		<h1 class="Profile-Header-Name">
			<a href="/" style="color:#fff;">
			<strong>
			< See all 
			</strong>
			my notes 
			</a>
		</h1>
	</div>
</div>

<div class="containter-wrapper">
	<div class="containter">			
		% #for i in user:
		<p> </p>
		% #end

		% if len(note) == 0:
			<h2>Empty. There's any Note here</h2>
		%else:
			<div class="Note" id="{{note['NoteID']}}">

				<h1 class="singleNote-Title">
					{{note['Title']}}
					
				</h1>
				<p class="singleNote-Content">
					{{note['Content']}}
				</p>
				<p class="singleNote-Content">
					<b>Published</b> on {{note['CreatedAt']}}
					% if (note['Private']):
						<span class="Note-Private">
							- Private Note
						</span>
					% end
				</p>

				
				% if user != None and user['UserID'] == note['UserID']:
					<p class="singleNote-Content">
						<a href="/{{user['Username']}}/{{note['Permalink']}}/edit">Edit note</a>
						|
						<a href="/delete/{{note['NoteID']}}">Delete note</a>
					</p>
				% end

			</div>
			
		% end
		</div>
	</div>


% include ('footer.tpl')
