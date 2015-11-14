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
				<a href="/">SudoNotes</a>
			</div>
			<div class="Header-options">

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

				% if user != None:
					<div class="Header-options-profileLink" id="dropdownMenu">
						<a href="/"><p>{{user['Name']}} {{user['Surname']}} ▾</p></a>
					
						<ul class="Header-options-menu">

							% if user != None:
								<li class="Header-options-menu-button">
									<a href="/{{user['Username']}}">My notes</a>
								</li>
								<li class="Header-options-menu-button">
									<a href="/profile">Profile</a>
								</li>
								<li class="Header-options-menu-button">
									<a href="/profile/edit">Edit profile</a>
								</li>
								<li class="Header-options-menu-button">
									<a href="/logout">Log out</a>
								</li>
							% else:	
								Create an account | Login
							% end

						</ul>
					</div>
				%end

			</div>
		</div>
	</div>
	 
	<div class="reader-Wrapper">
		<div class="reader">
			<div class="reader-close">Close</div>
			<h1 class="reader-Title">Title</h1>
			<p  class="reader-Content">Content</p>

			<div id="reader-loader"><img src="/images/loading.gif"></div>
		</div>
	</div>