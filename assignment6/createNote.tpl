% include ('header.tpl', title='Hola')

		<style type="text/css">
			.note-Title {
				width: 100%;
				min-height: 100px;
				font-size: 100px;
				font-family: arial;
				border:0;
				outline: 0;
				background: transparent;
			}
			.note-Content {
				width: 100%;
				min-height: 200px;
				font-size:30px;
				font-family: arial;
				border:0;
				outline: 0;
				background: transparent;
			}
			.note-save {
				padding: 10px 20px;
				font-size: 20px;
				background: #f4f4f4;
				color: #000;
				border:0;
			}
		</style>

<div class="containter-wrapper">
	<div class="containter">			

		% if editNote == True:
		<form action="/update/{{note['NoteID']}}" method="POST"> 
		%else:
		<form action="/create" method="POST"> 
		%end
			
			% if editNote == True:
			<h1>Edit your note</h1>
			%else:
			<h1>Create your note</h1>
			%end

			<div>
				%print note
				% if editNote == True:
					<input id="noteTitle" class="note-Title" name="titleNote" required="required" type="text" placeholder="Title of the note" value="{{note['Title']}}" />
				%else:
					<input id="noteTitle" class="note-Title" name="titleNote" required="required" type="text" placeholder="Title of the note" value="" />
				%end
			</h1>
			<p>

				% if editNote == True:
					<textarea id="noteContent" class="note-Content" name="contentNote" required="required" type="text" placeholder="Start writing your note..." value="{{note['Content']}}">{{note['Content']}}</textarea>
				%else:
					<textarea id="noteContent" class="note-Content" name="contentNote" required="required" type="text" placeholder="Start writing your note..."></textarea>
				%end
				
			</p>

			<p class="signin button"> 

				% if colors != None: 
					% if editNote == True:
						Current color: {{note['Color']}} <br />
						Change to:
						<select name="colorNote">
						% for color in colors:
						  <option value="{{color['Name']}}">{{color['Name']}}</option>
						% end
						</select>
					%else:
						<select name="colorNote">
						% for color in colors:
						  <option value="{{color['Name']}}">{{color['Name']}}</option>
						% end
						</select>
					%end
				% end
			</p>


			<p class="signin button"> 
				Private Note <input type="checkbox" name="privateNote" value="1" class="note-publish"/> 

				% if editNote == True:
					<input type="submit" class="inputField" value="Update note"/> 
				%else:
					<input type="submit" class="inputField" value="Publish note"/> 
				%end
			</p>
 

			<p class="change_link">  
				Already a member ?
				<a href="/login" class="to_register"> Go and log in </a>
			</p>
		</form>

		
		</div>
	</div>


% include ('footer.tpl')
