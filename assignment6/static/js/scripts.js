// notesID 	= []; // All the ID's for notes of a user
readerWrapper = $('.reader-Wrapper'); // Modal box showed each time user click on a note.
reader 		  = $('#reader');
readerContent = $('.reader-Content');
readerLoader  = $('#reader-loader')
previewClose  = $('.reader-close');

previewClose.click(function() {
	hidePreviewNote();
});

$(document).keyup(function(e) {
     if (e.keyCode == 27) { // escape key maps to keycode `27`
        hidePreviewNote();
    }
});

$( ".Note-wrapper" ).each(function( index ) {
	
	var Note = $(this)
	var NoteInfo = undefined;
	var NoteID = $(this).find('.Note').attr('id');
	var NoteOptions = Note.find('.Note-Options');
	var NoteDropdown = Note.find('.Note-Options-dropDown');

	// Show dropdown menu
	function dropDown () {
		NoteDropdown.toggleClass('Note-Options-dropDown-display');
	}
 
	// Config button that opens the dropdown menu
	$('.Note-Options-delete', this).click(function(e) {
		toDelete = confirm("Are you sure you want to delete this note?");
		if (toDelete) {
			url = 'api/notes/delete/' + String(NoteID)
			deleteNote(url);
			refresh();
		}

		return false;
	}); 

	// DELETE ONE NOTE
	$(".Note-Options-link", this).click(function(e) {
		dropDown();
		return false;
	}); 

	// When clicked on "Note-link" open the Note in current window
	$(".Note-link", this).click(function(e) {
		
		note = $(this).parent();
		NoteID = note.attr('id');
		noteTitle = note.find('.Note-Title').html()
		noteContent = note.find('.Note-Content').html()
		noteInfo = "";

		url = 'api/notes/' + String(NoteID)
		readerLoader.fadeIn('200');

		readerContent.hide('0');
		readerLoader.fadeIn('200');

		$.getJSON( url, function( data ) {
			if (data['valid'] == "false") {
				message = data['status'];
				alert(message);
			}
			else {
				changePreviewData(data); // Set note data on reader
				displayPreviewNote(); // Show the reader
				changeURL('#/' + data['Permalink'] + '/' + data['NoteID']);
			}
		})
		.error(function() {
			alert("Sorry... We couldn't retrieve information for that note... Try later")
		})
		.complete(function() { 
			readerLoader.hide(0);
			readerContent.delay(100).fadeIn('200');
		});

		return false;
	});

});

function deleteNote(apiUrl) {

	readerContent.hide('0');
	readerLoader.fadeIn('200');

	$.getJSON( apiUrl, function( note ) {
		message = note['status'];
		valid   = note['valid'];
		deleted = note['deleted'];

		if (deleted == "false") {
			alert(message);
		}
		else {
			alert(note['status']);
			changeURL('#/' + note['Permalink'] + '/' + data['NoteID']);
		}
	})
	.error(function() {
		alert("Sorry... We couldn't retrieve information for that note... Try later")
	})
	.complete(function() { 
		readerLoader.fadeOut('200');
		readerContent.delay('200').fadeIn('200');
	});

}

function displayPreviewNote() {
	reader.delay('2000').addClass('reader-ZoomIn', 'slow', 'easeInOutElastic');

	topHeight = scrollY + 100;
	reader.css({
	    position:'absolute',
	    top: topHeight
	    // left:700 + 60 + (($(window).width()-940) / 2), 
	});

	readerWrapper.fadeIn('slow', 'easeInOutElastic');
}
function hidePreviewNote() {
	changeURL('#/');
	reader.removeClass('reader-ZoomIn', 'slow', 'easeInOutElastic');
	readerWrapper.fadeOut('slow', 'easeInOutElastic');
}
function changePreviewData(note) {
	// Use the box ide to get the text of title...
	$('#reader-Title').html(note['Title']);
	$('#reader-Content').html(note['Content']);
}

function changeURL (Permalink) {
	window.location = String(Permalink);
} 


window.ColorLuminance = function(hex, lum) {

	// validate hex string
	hex = String(hex).replace(/[^0-9a-f]/gi, '');
	if (hex.length < 6) {
		hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
	}
	lum = lum || 0;

	// convert to decimal and change luminosity
	var rgb = "#", c, i;
	for (i = 0; i < 3; i++) {
		c = parseInt(hex.substr(i*2,2), 16);
		c = Math.round(Math.min(Math.max(0, c + (c * lum)), 255)).toString(16);
		rgb += ("00"+c).substr(c.length);
	}

	return rgb;
}


