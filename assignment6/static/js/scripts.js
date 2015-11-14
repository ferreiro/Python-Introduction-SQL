// notesID 	= []; // All the ID's for notes of a user
readerWrapper = $('.reader-Wrapper'); // Modal box showed each time user click on a note.
reader = $('.reader');
previewClose = $('.reader-close');
 
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

	function displayConfig () {
		NoteOptions.show('0');
	}
	// Show dropdown menu
	function dropDown () {
		NoteDropdown.toggleClass('Note-Options-dropDown-display');
	}
 
	// Config button that opens the dropdown menu
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
		$('#reader-loader').fadeIn('200');

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
			$('#reader-loader').fadeOut('200');
		});

		return false;
	});

});

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
	$('.reader-Title').html(note['Title']);
	$('.reader-Content').html(note['Content']);
}

function changeURL (Permalink) {
	window.location = String(Permalink);
} 


