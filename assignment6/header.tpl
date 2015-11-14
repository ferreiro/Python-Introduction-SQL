<!DOCTYPE html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>SuperNotes</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link href='https://fonts.googleapis.com/css?family=Raleway:400,500,700|Open+Sans:400,700,600|Roboto:400,300,500,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/profile.css">
 
  <!--[if lt IE 9]>
  <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->
</head>
<body>

	<div class="Header-wrapper">
		<div class="Header">
			<div class="Header-logo">
				<a href="/">
					<p>SudoNotes</p>
				</a>
			</div>
			<div class="Header-options">

				% if user != None:
				<div class="Header-options-search">
					<form action="/search" method="POST">
						<p> 
							<input id="searchText" name="query" required="required" type="text" placeholder="Search by title or content..." /> 
						</p>
					</form>
				</div>

				<div class="Header-options-createNote">
					<a href="/create"><p>Create note</p></a>
				</div>
				% end

				% if user == None:

				<div class="Header-options-button button-login">
					<a href="/login">
						<div class="Header-options-button-icon">
							<span class="icon-locked"></span>
						</div>
						<p class="Header-options-button-title">
							Login
						</p>
					</a>
				</div>

				<div class="Header-options-button button-register">
					<a href="/register">
						<div class="Header-options-button-icon">
							<span class="icon-enter"></span>
						</div>
						<p class="Header-options-button-title">
							Register
						</p>
					</a>
				</div>
				
				% end

				% if user != None:

					<%

						# import code for encoding urls and generating md5 hashes
						import urllib, hashlib
						
						# Set your variables here
						
						email 	= user['Email'];
						default = "images/default.png"
						size 	= 100
 						 
						# construct the url
						gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
						gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

						print gravatar_url

					%>

					
					<div class="Header-options-myprofile" id="dropdownMenu">
						<a href="/profile" class="Header-options-myprofile-resume" >
							<span class="Header-options-myprofile-resume-avatar">
								<img src="{{gravatar_url}}"/>
							</span>
							<p class="Header-options-myprofile-resume-name">
								{{user['Name']}} {{user['Surname']}}
							</p>
							<span>▾</span>
						</a>
					
						<ul class="Header-options-myprofile-menu">

							<li class="Header-options-myprofile-menu-list">
								<a href="/{{user['Username']}}">My notes</a>
							</li>
							<li class="Header-options-myprofile-menu-list">
								<a href="/profile">Profile</a>
							</li>
							<li class="Header-options-myprofile-menu-list">
								<a href="/profile/edit">Edit profile</a>
							</li>
							<li class="Header-options-myprofile-menu-list">
								<a href="/logout">Log out</a>
							</li>

						</ul>
					</div>
				%end

			</div>
		</div>
	</div>
	 
	<div class="reader-Wrapper">
		<div class="singleNote" id="reader">
			<div class="reader-close" id="reader-close">
				<span class="icon-close"></span>
			</div>
			
			<div class="reader-loader" id="reader-loader"></div>

			<div class="reader-Content">
				<h1 class="singleNote-Title" id="reader-Title">Title</h1>
				<p class="singleNote-Content" id="reader-Content">Content</p>
			</div>
			
		</div>
	</div>