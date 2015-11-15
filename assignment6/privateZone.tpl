% include ('header.tpl', title='Hola')

<div class="Profile-Header-wrap">
	<div class="Profile-Header">	
		<h1 class="Profile-Header-Name">
			<strong>Private zone</strong><br />
			You are trying to accessing a private zone.<br />
			
			%print user
			% if user != None:
				<a href="/profile" style="color:#fff; text-decoration:underline;">Go to your profile</a>
			% else:
				<a href="/login" style="color:#fff; text-decoration:underline;">Login in</a>
				or 
				<a href="/register" style="color:#fff; text-decoration:underline;">Create free account</a>
			% end
		</h1>
	</div>
</div>


% include ('footer.tpl')

		